import socketio
import threading

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server!')
    print('Type your messages (or "quit" to exit):')

@sio.on('chat')
def on_chat(data):
    print(f'\nReceived: {data}')
    print('Me: ', end='', flush=True)

@sio.on('disconnect')
def on_disconnect():
    print('\nDisconnected from server')

def send_messages():
    while sio.connected:
        try:
            message = input('Me: ')
            if message.lower() == 'quit':
                sio.disconnect()
                break
            sio.emit('message', message)
        except EOFError:
            break

if __name__ == '__main__':
    try:
        sio.connect('http://localhost:5000')
        send_messages()
    except socketio.exceptions.ConnectionError as e:
        print("Connection Error! Make sure the server is running.")
    except KeyboardInterrupt:
        print("\nExiting...")
        sio.disconnect()