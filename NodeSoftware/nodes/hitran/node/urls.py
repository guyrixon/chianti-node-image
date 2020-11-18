from django.conf.urls.defaults import *
from nodes.hitran.node import views
from django.conf import settings
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(settings.NODENAME+'.node.views',
                (r'^$', 'index'),
                (r'^tap/', include('vamdctap.urls')),
                )

# Replace the base by your node name and add urls
# if you have custom views.
#urlpatterns + = patterns('DjExampleNode.node.views',
#                       (r'^$', 'index'),
#                       )

