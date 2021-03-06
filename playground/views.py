from django.shortcuts import render_to_response
from django.template import RequestContext

#Unused import to load all the socketio gevent implementations

from playground.socketioplayground import *


def echo(request):
    return render_to_response('playground/echo.html',
        context_instance=RequestContext(request))


def time(request):
    return render_to_response('playground/time.html',
        context_instance=RequestContext(request))


def chat(request):
    return render_to_response('playground/chat.html',
        context_instance=RequestContext(request))
