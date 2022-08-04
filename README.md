Files to make the Docker image that runs the Chianti node of VAMDC.

This node uses :
* Python node-software (snapshot included in this repository);
* Chianti-7 data, packed in an SQLite database;
* Gunicorn as a web server.

Running the image in a container generates the complete node; there is
no separate DB container.

The Gunicorn server is conventionally run on an unprivileged port for HTTP
with traffic redirected from port 80 by a reverse proxy. HTTPS is not
supported. See the deployment note in this repository for details.
