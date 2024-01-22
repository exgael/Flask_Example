.PHONY: helloworld message_server message_terminal install clean

helloworld:
	./helloworld/venv/bin/python3 ./helloworld/app.py

message_server:
	./messages/backend/venv/bin/python3 ./messages/backend/app.py

message_terminal:
	./messages/frontend/venv/bin/python3 ./messages/frontend/terminal.py

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

clean:
	@echo "Cleaning up..."
	rm -rf ./helloworld/venv
	rm -rf ./messages/backend/venv
	rm -rf ./messages/frontend/venv
	@echo "Cleaned."