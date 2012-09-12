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
        self.broadcast_event('receive msg', user, msg)
        return True

    def on_connected(self, user):
        print('User %s connected' % user)
        self.socket.session['nick'] = user
        self.broadcast_event('user connected', user)
