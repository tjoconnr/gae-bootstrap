#!/usr/bin/env python
from google.appengine.ext import db
from app.models import BaseModel 

class HelloWorldModel(BaseModel):
    name = db.StringProperty(required=True)            
