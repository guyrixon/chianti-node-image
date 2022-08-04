The standard, operational configuration for the Chianti node is
Gunicorn running as a Docker-swarm service on port 8001 and 
Apache running on port 80 as a reverse proxy. The node is 
confined to a single server.

It is possible to Gunicorn on port 80, directly exposed to the
Internet. This is not done for Chianti, firstly because there
are other web resources that need to be accessible from port 80,
and secondly because Gunicorn is not considered wholly secure
when exposed directly to the internet.

For historical reasons, the reverse proxy is Apache2. Nginx
would be a better choice for a new installation. Details of the
reverse proxy stated here refer to Apache, but the same effect
is obtainable on the other kind of server.

# Reverse proxy

It is hard to set up a reverse proxy in a container: there are
too many problems with network access and IP addresses. Therefore,
Apache is installed directly on the Ubuntu host, using the
apache2 package from the Ubuntu repository.

No vhost is used for the Chianti service; there is no corresponding
file in sites-available. Instead, a configuration file for the Chianti
reverse-proxy is added to /etc/apache2/conf-available:

	ProxyPreserveHost Off

	ProxyPass /chianti7 http://127.0.0.1:8001/chianti7
	ProxyPass /chianti7/ http://127.0.0.1:8001/chianti7/
	ProxyPassReverse /chianti7/ http://127.0.0.1:8001/chianti7/
	ProxyPassReverse /chianti7 http://127.0.0.1:8001/chianti7
	
It's unclear whether the ProxyPassReverse lines are actually 
needed for this type of service.

ProxyPreserveHost must be off.

Note that the path to the service is unchanged by the proxy. This
is essential. If the path be changed, most of the node works
but any resource generated with an embedded, absolute URL back
to the node has the wrong path in that URL. This is a general
principle for reverse proxies: they are too stupid to correctly
adjust paths and any path adjustment must be assigned to a component
that better understands the architecture.

# Docker service

The node is deployed as a WSGI application in Gunicorn, with an
embedded database (using SQLite). The whole runs in one container.

The container is obtained from a Docker swarm service.

	docker swarm service create --name chianti-node \
	    -p 8001:8000 \
	    -e "SCRIPT_NAME=/chianti7" \
	    guyrixon/vamdc-chianti-node:8.3
	    
The port 8001 for HTTP is set to match the reverse proxy and there is no 
HTTPS port. The node software uses port 8000 inside the container and
this is published to a different port to allow for later installation
of other nodes on the same host.

The environment variable SCRIPT_NAME is also set to match the 
reverse proxy. The node software runs the WSGI application at the root
path, i.e. http://localhost:8001/. Gunicorn, as a WSGI server, understands 
the context well enough to make the path adjustment to and from
http://localhost:8001/chianti7. The reverse proxy doesn't work
completely if the paths in the internal and external URLs don't match.

There are no data volumes for this service because the static database
is included in the container image. There are no Docker secrets for the
service because the database is not accessible outside the container and
needs no password. There are no network specifications because the service
publishes its HTTP port on the host; no container-to-container connections
are needed.

# Adjustments to node software

The node software in this deployment is a snapshot of the repository
VAMDC/NodeSoftware on Github.

There are no adjustments to the common parts of the node software.

In the node-specific settings for Chianti, a line is added:

	USE_X_FORWARDED_HOST = True
	
In modern versions of Django, this is necessary to work correctly with 
a reverse proxy. It refers to the HTTP header X-FORWARDED-HOST which is
normally only present when a reverse proxy is used.