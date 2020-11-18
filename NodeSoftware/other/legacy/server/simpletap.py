#!/usr/bin/env python
"""

simple.py

Very basic proof-of-concept implementation of a webserver that
answers a data query that it gets via a HTTP POST request by handing
it to a SQLite database and sending the data back.

"""

from SimpleHTTPServer import SimpleHTTPRequestHandler, BaseHTTPServer
from cgi import parse_qsl as parse
import simplejson as j
from sqlite3 import dbapi2 as sqlite
import string as s
from sys import argv,exit
import vamdc.xmltools.valdxsams as vx


class MyHandler(SimpleHTTPRequestHandler):
    """
        The class that gets bound to the webserver
    """
    
    def do_POST(self):
        """
            handle POST requests, pepending on the URL.
        """
        if self.path=='/tap/sync':
            self.answer_query()
        elif self.path=='/tap/registry':
            self.answer_registry()
        else:
            self.e404()

    def e404(self):
        """
            a proper 404 reply for unknown requests
        """
        self.send_response(404)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('Error 404')

    def answer_registry(self):
        """ 
           answer a registry request. not yet implemented.
        """
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('to be implemented')
        
    def answer_query(self):
        """
            answer data query by parsing the request, 
            handing it to runquery() and sending the
            json-encoded data back.
        """
        length= int( self.headers['content-length'] )
        quer=self.rfile.read( length )
        self.quer=parse(quer)
        self.log_message("""post data is: %s"""%str(self.quer))
        self.send_response(200)
        #self.send_header('Content-type','text/html')
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        j.dump(self.runquery(),self.wfile)
        
    def do_GET(self):
        """
           GET requests are not wanted.
        """
        self.e404()

    def runquery(self):
        """ Takes the list with the parsed request and constructs
            the SQL query from it, then runs it. Returns the data
            together with the column names.
        """
        for quer in self.quer:
            if quer[0]=='QUERY':
                query=quer[1]
            else:
                continue
        #print query

        return vx.run(curs,query)

        
def run(argv):
    """
        connect to the DB and start the server
    """
    global curs

    if len(argv) > 1:
        DBNAME=argv[1]
    else:
        DBNAME='dummy.db'

    try:
        conn=sqlite.connect(DBNAME)
        curs=conn.cursor()
        print 'bound to %s'%DBNAME
    except:
        print 'Error in opening the database: %s'%argv[1]
        exit(1)

    try:
        server = BaseHTTPServer.HTTPServer(('', 8081), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    run(argv)
