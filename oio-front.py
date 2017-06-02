#!/usr/bin/env python

#from oiopy import object_storage
import tornado.ioloop
import tornado.web
import tornado.httpserver
#from tornado.simple_httpclient import SimpleAsyncHTTPClient
#from tornado.httpclient import AsyncHTTPClient
from oio.api.object_storage import ObjectStorageAPI
from tornado.httpclient import HTTPClient, HTTPError, AsyncHTTPClient
from PIL import Image
import random
import string
from tornado.log import enable_pretty_logging
import json
import time
import cStringIO as StringIO

OIONS = "OPENIO"
OIOACCOUNT = "ACCOUNT_WRITE"

random_chars = string.ascii_lowercase + string.ascii_uppercase +\
            string.digits

def random_str(n, chars=random_chars):
    return ''.join(random.choice(chars) for _ in range(n))

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, oions, oioaccount, oioproxy):
        self.oions = oions
        print self.oions
        self.oioaccount = oioaccount
        print self.oioaccount
        self.oioproxy = oioproxy
    def get(self):
        print "NS: %s"%self.oions
        print self.oioaccount
        print self.oioproxy
        #self.write(self.request.uri)

        self.set_header("Access-Control-Allow-Origin", "*")
        contentL_present = 0
        multidescr = 0
        mime_type = ""
        storage = ObjectStorageAPI(self.oions, "http://192.168.1.174:6006")
        #http_client = AsyncHTTPClient()
        http_client = HTTPClient()
        container = self.request.uri.split("/")[1]
        if len(self.request.uri.split("/", 2)) > 2:
            obj = self.request.uri.split("/", 2)[2]
        #print self.request.uri.split("/", 2)[2]
        #print("container %s"%container)
        length = 0
        try:
            start = time.time()
            meta, stream = storage.object_fetch(self.oioaccount, container, obj)
            delay = time.time() - start
            print("read from storage time: %5.3f ms"%(delay*1000))
            #print "meta:"
            #print meta
            mime_type = meta['mime_type']
            length = meta["length"]
            #print meta['properties']
            for k, v in meta['properties'].iteritems():
                if k != 'componentsconfiguration':
                    #print("%s %s"%(k,v))
                    self.set_header(k, v)
        except Exception as e:
            #print "pb"
            print e
            self.clear()
            self.set_status(500)
            self.finish("<html><body>%s</body></html>"%e)
        else:
            print("from cache")
            for chunk in stream:
                self.write(chunk)

            if mime_type:
                #print mime_type
                self.set_header('Content-Type', mime_type)
            if length:
                #print length
                self.set_header('Content-Length', length)
            self.finish()
        #tornado.ioloop.IOLoop.instance().add_callback(self.loop)

def make_app():
    args = {
        'oions': OIONS,
        'oioaccount': OIOACCOUNT,
        'oioproxy': "192.168.1.174"
        }
    return tornado.web.Application([
        (r"/.*$", MainHandler, args),
    ])

if __name__ == "__main__":
    enable_pretty_logging()
    server = tornado.httpserver.HTTPServer(make_app())
    server.bind(8282)
    server.start(0)
    try:        
        print 'running on port %s' % 8282
        tornado.ioloop.IOLoop.instance().start()

    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
