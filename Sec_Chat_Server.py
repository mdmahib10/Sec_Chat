import socketio
import eventlet

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
    print('Server Starting....')
    print('Listening on http://0.0.0.0:5000')
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)