#!/usr/bin/env python

import config
import requests

base_url = "https://api.africastalking.com/version1/user"

headers = dict(Apikey=config.apikey, Accept= "application/xml")

payload = dict(username = "pystar")

result = requests.get(base_url, headers=headers, params=payload)

print(result.status_code)

print(result.text)


