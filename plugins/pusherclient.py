#!/usr/bin/python3

import time
import queue
from threading import Thread
from pusher import Pusher
import config
import logging.config
import pusherclient
import json
from pusher import Pusher


logging.config.dictConfig(config.log)
logger = logging.getLogger(__name__)

CLIENT_SECRETS_FILE = "client_secrets.json"


class Plugin():
    def __init__(self, bus):
        self.bus = bus
        with open(CLIENT_SECRETS_FILE) as data_file:    
            data = json.load(data_file)
            
        self.p = pusherclient.Pusher(data['pusher']['key'])
        self.pusher = Pusher(app_id=data['pusher']['app_id'], key=data['pusher']['key'], secret=data['pusher']['secret'])
        
        self.p.connection.bind('pusher:connection_established', self.connect_handler)
        self.p.connect()

        fmap = { 'score_goal': self.score,
                 'win_game': self.score,  
                 'reset_score': self.score  }
        self.bus.subscribe_map(fmap, thread=False)
    
    def run(self):
        while True:
            # Do other things in the meantime here...
            time.sleep(1)
        
    def score(self, event):
        self.pusher.trigger('foosball','score_goal',event)

    def connect_handler(self, data):
        channel = self.p.subscribe(config.pusher_channel)
        channel.bind('start_game', self.start_game)
        channel.bind('simulate_score', self.simulate_score)

    def simulate_score(self, env):
        data = json.loads(env)
        self.bus.notify('goal_event', {'source': 'serial', 'team': 'yellow', 'duration': 100001})
        
    def start_game(self, env):
        data = json.loads(env)
        self.bus.notify("set_game_mode", {"mode": data["mode"] })
        self.bus.notify("reset_score")
        self.bus.notify("set_players",{'black':data["black"], 'yellow':data["yellow"]})
        logger.info("Pusher Event: %s", data)

#{
#  "yellow": ["Nilhouse", "Keith"],
#  "black": ["MrsHammer", "Maximus"],
#  "mode": 5
#}

#       self.bus.notify("set_game_mode", {"mode": 5 })
#       self.bus.notify("reset_score")
#       self.bus.notify("set_players",{'black':['Nils','Max'], 'yellow':['Arlington','Keith']})
