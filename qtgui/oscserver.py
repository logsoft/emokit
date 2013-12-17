__author__ = 'hpl'
#!/usr/bin/env python
from liblo import *
import sys

class MyServer(ServerThread):
    def __init__(self):
        ServerThread.__init__(self, 12321)

    @make_method('/emotiv/', 'i')
    def foo_callback(self, path, args):
        i, f, s = args
        print "received message '%s' with arguments: %d," % (path, i)

    @make_method(None, None)
    def fallback(self, path, args):
        print "received unknown message '%s' : '%s" % (path,args)

try:
    server = MyServer()
except ServerError, err:
    print str(err)
    sys.exit()

server.start()
raw_input("press enter to quit...\n")
