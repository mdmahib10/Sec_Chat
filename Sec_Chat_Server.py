import socketio
import eventlet
import socket

# Create the Socket.IO server
sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print(f'Client connected: {sid}')

@sio.on('message')
def message(sid, data):
    print(f'{sid}: {data}')
    sio.emit('chat', data, skip_sid=sid)  # Broadcast to all except sender
    
@sio.on('disconnect')
def disconnect(sid):
    print(f'Client disconnected: {sid}')

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    print('Server Starting....')
    print(f'Listening on http://{ip}:5000')
    eventlet.wsgi.server(eventlet.listen((ip, 5000)), app)