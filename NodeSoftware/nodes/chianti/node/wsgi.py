"""
WSGI-configuration module for the VAMDC node-software of the Chianti node

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/

To activate this module in gunicorn run

  gunicorn node.wsgi

from an environment where the gunicorn modules and scripts are installed.
Note that the argument is a reference to this module, and the module must be on
the Python path. Therefore, add to the path both the directory holding Chianti's
settings.py and the directory called NodeSoftware holding the entire node-software
collection.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nodes.chianti.settings")
application = get_wsgi_application()
