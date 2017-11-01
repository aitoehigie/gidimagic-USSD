#!/usr/bin/env python

import config
import requests
from gateway import AfricasTalkingGateway, AfricasTalkingGatewayException
username="sandbox"
apikey="46270a110ed943cd3cf4d2093f5ddb6a8cf9e76636ae46fc58e6d6219c1e74a8"
mygateway = AfricasTalkingGateway(username, apikey, "sandbox")
to="+2348029401212"
message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"


try:
    # Thats it, hit send and we'll take care of the rest.
    
    results = mygateway.sendMessage(to, message)
    
    for recipient in results:
        # status is either "Success" or "error message"
        print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                            recipient['status'],
                                                            recipient['messageId'],
                                                            recipient['cost'])
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while sending: %s' % str(e)


try:
    user = mygateway.getUserData()
    print user['balance']
    # The result will have the format=> NGN XXX
except AfricasTalkingGatewayException, e:
    print 'Error: %s' % str(e)

