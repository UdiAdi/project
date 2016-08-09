"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/UdiAdi/myblog/project/settings.py'
path = '/home/UdiAdi/myblog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.project.settings'

## Uncomment the lines below depending on your Django version
###### then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

