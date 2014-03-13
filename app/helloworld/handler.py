#!/usr/bin/env python
from google.appengine.api import users

from app.handler import BaseHandler

class HelloWorldHandler(BaseHandler):
    def get(self, page_name):          

    	# Get currently logged in Google user
    	current_user = users.get_current_user()                                        

        template_values = {
        	'user': current_user,
			'logout_url': users.create_logout_url("/"),
			'login_url': users.create_login_url("/")
        }

        if not page_name: page_name = "index"        
        self.render("%s.html" % (page_name), **template_values)