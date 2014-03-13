#!/usr/bin/env python
import json
import time
from datetime import datetime,date

from google.appengine.ext import db

class BaseModel(db.Model):
    def to_dict(self):
        SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)
        output = {}
        output["id"] = self.key().id()
        for key, prop in self.properties().iteritems():        
            value = getattr(self, key)
            if value is None or isinstance(value, SIMPLE_TYPES):
                if isinstance(value, list) and not all(isinstance(x,(int,unicode,str,float)) for x in value):
                    output[key] = [str(i.id()) for i in value]                    
                else:
                    output[key] = value            
            elif isinstance(value, date):
                # Convert date/datetime to MILLISECONDS-since-epoch (JS "new Date()").
                ms = time.mktime(value.utctimetuple()) * 1000
                ms += getattr(value, 'microseconds', 0) / 1000
                output[key] = int(ms)
            elif isinstance(value, db.GeoPt):
                output[key] = {'lat': value.lat, 'lon': value.lon}
            elif isinstance(value, BaseModel):
                output[key] = value.to_dict()
            else:
                raise ValueError('cannot encode ' + repr(prop))
        return output

    def to_json(self):
        return json.dumps(self.to_dict(),sort_keys=True,indent=5)