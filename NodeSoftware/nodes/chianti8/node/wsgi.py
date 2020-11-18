"""
WSGI config

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/Users/guy/git/VAMDC/NodeSoftware')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nodes.chianti.settings")
application = get_wsgi_application()
