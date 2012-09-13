from socketio.handler import SocketIOHandler
from socketio.sgunicorn import GeventSocketIOWorker


class GeventWebSocketWorker(GeventSocketIOWorker):
    wsgi_handler = SocketIOHandler
