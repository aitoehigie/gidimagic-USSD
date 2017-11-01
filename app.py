#!/usr/bin/env python

import config
from config import username, apikey
import requests
from gateway import AfricasTalkingGateway, AfricasTalkingGatewayException

mygateway = AfricasTalkingGateway(username, apikey, "sandbox")
to="+2348029401212"
message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"


try:
    user = mygateway.getUserData()
    print user['balance']
    # The result will have the format=> NGN XXX
except AfricasTalkingGatewayException, e:
    print 'Error: %s' % str(e)

