#!/usr/bin/python
import requests, sys, json
dd_api_key = "<api key>"
dd_datacenter = "us" # 'us' or 'eu'
headers = {'Content-Type': 'text/plain'}

if dd_datacenter == "us":
    endpoint = "https://http-intake.logs.datadoghq.com/v1/input/{}".format(dd_api_key)
else:
    endpoint = "https://http-intake.logs.datadoghq.eu/v1/input/{}".format(dd_api_key)

payload = sys.argv[1]
try:
    payload2 = json.loads(payload)
    headers = {'Content-Type': 'application/json'}
except ValueError as e:
    headers = {'Content-Type': 'text/plain'}

tags = "ddtags=" + sys.argv[2]
response = requests.post(endpoint, headers=headers, params=tags, data=payload)