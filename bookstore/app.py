import os
from flask import Flask, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_json_schema import JsonSchema, JsonValidationError
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from functools import wraps

def requires_role(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                return jsonify({'message': 'Permission denied'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

app = Flask(__name__)

### JSON SCHEMA

add_book_schema = {
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
        'author': {'type': 'string'},
        'published_year': {'type': 'integer'},
    },
    'required': ['title', 'author', 'published_year']
}
jsonschema = JsonSchema(app)

### DATABASE

app.config['SECRET_KEY'] = 'your_secret_key'
base_dir = os.path.abspath(os.path.dirname(__file__))
os.makedirs(os.path.join(base_dir, 'instance'), exist_ok=True)
db_path = os.path.join(base_dir, 'instance/books.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## AUTH

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')  # 'user' or 'moderator'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


### AUTH ROUTES

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'], role=data.get('role', 'user'))
    db.session.add(new_user)
    db.session.commit()
    flash('Registration successful. Please log in.')
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/register_moderator', methods=['POST'])
def register_moderator():
    data = request.json
    new_moderator = User(username=data['username'], password=data['password'], role='moderator')
    db.session.add(new_moderator)
    db.session.commit()
    flash('Moderator registration successful. Please log in.')
    return jsonify({'message': 'Moderator registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

### API ROUTES

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year
        }

@app.route('/books', methods=['POST'])
@login_required
@requires_role('moderator')
@jsonschema.validate(add_book_schema)
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], published_year=data['published_year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books', methods=['GET'])
@login_required
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:id>', methods=['GET'])
@login_required
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())

@app.route('/books/<int:id>', methods=['PUT'])
@login_required
@requires_role('moderator')
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    book.title = data['title']
    book.author = data['author']
    book.published_year = data['published_year']
    db.session.commit()
    return jsonify(book.to_dict())

@app.route('/books/<int:id>', methods=['DELETE'])
@login_required
@requires_role('moderator')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 204

@app.errorhandler(JsonValidationError)
def on_validation_error(e):
    return jsonify({'error': e.message}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8000, debug=True)
