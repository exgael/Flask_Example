from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return 'Real-Time Flask App'

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    print(f'Message received from {username}: {message}')
    emit('chat_message', {'username': username, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=8000, debug=True)
