import socketio

sio = socketio.Client()
username = input("Enter your username: ")

@sio.event
def connect():
    print('Connection established')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('chat_message')
def on_message(data):
    print(f'\n{data["username"]}: {data["message"]}')
    print("Enter message (type 'exit' to disconnect): ", end='', flush=True)

sio.connect('http://localhost:8000')

try:
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        sio.emit('message', {'username': username, 'message': message})
except KeyboardInterrupt:
    print("Exiting...")
finally:
    sio.disconnect()
