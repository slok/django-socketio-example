from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import socketio.sdjango


urlpatterns = patterns('',
    url(r'^$', 'djangosocketioexample.views.index'),
    url(r'^playground/', include('playground.urls')),
    url(r'^socket\.io', include(socketio.sdjango.urls))
)

urlpatterns += staticfiles_urlpatterns()