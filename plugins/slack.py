#!/usr/bin/python3

import requests
import json

url = 'https://hooks.slack.com/services/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'

payload={"text": "A very important thing has occurred! <https://alert-system.com/alerts/1234|Click here> for details!"}

headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)
