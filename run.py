import os

from gevent import monkey
monkey.patch_all()
from django.core.wsgi import get_wsgi_application
from socketio.server import SocketIOServer

PORT = 9000

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
    "djangosocketioexample.settings")
application = get_wsgi_application()

if __name__ == '__main__':
    print('Listening on http://127.0.0.1:%s and on port 843 \
        (flash policy server)' % PORT)
    SocketIOServer(('', PORT), application,
        resource="socket.io").serve_forever()
