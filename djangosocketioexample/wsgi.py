import os

from gevent import monkey
monkey.patch_all()
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE",
    "djangosocketioexample.settings")
application = get_wsgi_application()
