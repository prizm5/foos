#!/usr/bin/python3

import requests
import json

url = 'https://hooks.slack.com/services/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'

payload={
    "username":"foosball",
    "text": "We Have a Winner!!!"}

headers = {'content-type': 'application/json'}
msg = {
  "yellow": ["Nilhouse", "Keith"],
  "black": ["MrsHammer", "Maximus"],
  "mode": 5
}
print "%s" msg.get('yellow')
#response = requests.post(url, data=json.dumps(payload), headers=headers)
