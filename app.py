#!/usr/bin/env python

import config
import requests
from gateway import AfricasTalkingGateway, AfricasTalkingGatewayException

mygateway = AfricasTalkingGateway("sandbox", config.apikey)

try:
    user = mygateway.getUserData()
    print user['balance']
    # The result will have the format=> NGN XXX
except:
    #print ('Error: %s' % str(e))
    pass



