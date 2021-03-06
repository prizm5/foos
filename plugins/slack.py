#!/usr/bin/python3

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
        self.bus = bus
        with open(CLIENT_SECRETS_FILE) as data_file:    
            data = json.load(data_file)
        self.url = data['pusher']['slack']
        fmap = { 'win_game': lambda d: self.send('win_game', d) }
        self.bus.subscribe_map(fmap, thread=True)

    def run(self):
        while True:
            # Do other things in the meantime here...
            time.sleep(1)
        
    def send(self, name, event):
        str = "We Have a Winner!!! \n {0} & {1}"
        headers = { 'content-type': 'application/json' }
        team = event["team"]
        players = event["players"]
        
        if players != None :
            p = players[team]
            msg = str.format(p[0],p[1])
            payload={
                "username":"foosball",
                "text": msg}
            logger.info(payload)
            response = requests.post(self.url, data=json.dumps(payload), headers=headers)