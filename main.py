#!/usr/bin/env python
import webapp2, sys

# Include /lib so we can keep third-party libraries separate, but import them as 'import oauth'
if 'lib' not in sys.path:
    sys.path[0:0] = ['lib']

from app.helloworld.handler import HelloWorldHandler

app = webapp2.WSGIApplication([
	('/(.*)', HelloWorldHandler)
], debug=True)
