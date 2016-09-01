#!/usr/bin/python3

import 
import time
import queue
from threading import Thread
import config
import logging.config
import json
import requests



logging.config.dictConfig(config.log)
logger = logging.getLogger(__name__)

CLIENT_SECRETS_FILE = "client_secrets.json"


class Plugin():
    def __init__(self, bus):
url = 

headers = {'content-type': 'application/json'}
msg = {
  "yellow": ["Nilhouse", "Keith"],
  "black": ["MrsHammer", "Maximus"],
  "mode": 5
}

winners = "We Have a Winner!!! \n {0} & {1}".format(msg.get('yellow')[0],msg.get('yellow')[1])
payload={
    "username":"foosball",
    "text": winners}


print(payload)
#response = requests.post(url, data=json.dumps(payload), headers=headers)