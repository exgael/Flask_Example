.PHONY: helloworld message_server message_terminal bookstore install clean

install:
	# Create a virtual environment for helloworld
	python3 -m venv ./helloworld/venv
	# Activate the virtual environment and install dependencies
	./helloworld/venv/bin/pip install -r ./helloworld/requirements.txt

	# Create a virtual environment for message app backend
	python3 -m venv ./messages/backend/venv
	# Activate the virtual environment and install dependencies
	./messages/backend/venv/bin/pip install -r ./messages/backend/requirements.txt

	# Create a virtual environment for message app frontend
	python3 -m venv ./messages/frontend/venv
	# Activate the virtual environment and install dependencies
	./messages/frontend/venv/bin/pip install -r ./messages/frontend/requirements.txt

	# Create a virtual environment for bookstore
	python3 -m venv ./bookstore/venv
	# Activate the virtual environment and install dependencies
	./bookstore/venv/bin/pip install -r ./bookstore/requirements.txt

helloworld:
	./helloworld/venv/bin/python3 ./helloworld/app.py

message_server:
	./messages/backend/venv/bin/python3 ./messages/backend/app.py

message_terminal:
	./messages/frontend/venv/bin/python3 ./messages/frontend/terminal.py

bookstore:
	./bookstore/venv/bin/python3 ./bookstore/app.py

populate-bookstore:
	./bookstore/venv/bin/python3 ./bookstore/populate.py

clean:
	@echo "Cleaning up virtual environments..."
	@find . -type d -name "venv" -exec rm -rf {} +
	@echo "Cleaned."

	@echo "Cleaning up instance directories..."
	@find . -type f -name "books.db" -exec rm -rf {} +
	@echo "Cleaned."