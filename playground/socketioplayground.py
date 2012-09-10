import datetime

from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.sdjango import namespace


@namespace('/echo')
class EchoNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):

    def initialize(self):
        print("Socketio echo session started")

    def on_echo(self, msg):
        print('Echo message')
        #Send to the user only
        self.emit('echo msg', msg)
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

    def on_say(self, msg):
        return True