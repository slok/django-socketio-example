from django.conf.urls import patterns, include, url
import socketio


urlpatterns = patterns('',
    url(r'^$', 'djangosocketioexample.views.index'),
    url(r'^playground/', include('playground.urls')),
    url(r'^socket\.io', include(socketio.sdjango.urls))
)
