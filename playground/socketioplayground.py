import datetime

from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.sdjango import namespace


@namespace('/echo')
class EchoNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):

    def initialize(self):
        print("Socketio echo session started")

    def on_echo_me(self, msg):
        print('Echo me \"%s\" message' % msg)
        #Send to the user only
        self.emit('echo msg', msg)
        return True

    def on_echo_all(self, msg):
        print('Echo all \"%s\" message' % msg)
        #Send to the user only
        self.broadcast_event('echo msg', msg)
        return True


@namespace('/time')
class EchoNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):

    def initialize(self):
        print("Socketio time session started")

    def on_update_time(self, garbage):
        print('Update time')
        self.broadcast_event('update client time', str(datetime.datetime.now()))
        return True


@namespace('/chat')
class EchoNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):

    def initialize(self):
        print("Socketio chat session started")

    def on_says(self, msg):
        user = self.socket.session['nick']
        print('%s says: \'%s\'' % (user, msg))
        color = self.socket.session['color']
        self.broadcast_event('receive msg', user, msg, color)
        return True

    def on_join(self, user, color):
        print('User %s connected with color %s' % (user, color))
        self.socket.session['nick'] = user
        self.socket.session['color'] = color
        self.broadcast_event('user connected', user, color)

    def recv_disconnect(self):
        print('User %s Disconnected' % self.socket.session['nick'])
        user = self.socket.session['nick']
        color = self.socket.session['color']
        self.broadcast_event('user disconnected', user, color)
        self.disconnect(silent=True)
