#!/usr/bin/env python

import config
from config import username, apikey
import requests


#mygateway = AfricasTalkingGateway(username, apikey, "sandbox")
base_url="https://api.africastalking.com/version1/user"
header = dict(apikey=apikey, Accept="appliaction/json")
payload = dict(username=username)

result = requests.get(baseurl, params=payload, headers=header)
print(result.text())
