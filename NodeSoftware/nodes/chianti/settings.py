#
# VAMDC-node config file
#
# You may customize your setup by copy&pasting the variables you want to 
# change from the default config file in nodes/settings_default.py to 
# this file. Try to only copy over things you really need to customize 
# and do *not* make any changes to settings_defaults.py directly. That 
# way you'll always have a sane default to fall back on (also, the 
# master file may change with updates).

from settings_default import *

# Comment out the following line once your node goes live.
DEBUG=True

###################################################
# Database connection
# Host 'chianti-db' is for use in Docker swarm.
###################################################
DATABASES = { 
  'default' : {
    'ENGINE'   : 'django.db.backends.mysql', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'
    'NAME'     : 'chianti7',
    'USER'     : 'vamdc',
    'PASSWORD' : '',
    'HOST'     : 'chianti-db',
    'PORT'     : ''
  }
}

#########################################
# Admin information
#########################################
ADMINS = (            ('Admin 1 Name', 'name1@mail.net'),
            ('Admin 2 Name', 'name2@mail.net'),
        )

EXAMPLE_QUERIES = ['SELECT ALL WHERE RadTransWavelength > 5000 AND RadTransWavelength < 5010']


STATIC_URL = '/static/'
