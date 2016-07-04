#!/usr/bin/python3

import time
import queue
from threading import Thread
from pusher import Pusher
import config

CLIENT_SECRETS_FILE = "client_secrets.json"


class Plugin():
    def __init__(self, bus):
        p = Pusher(app_id=u'119859', key=u'76abfc1ad02da9810a9d', secret=u'07c4c701b5d1c864459d')
        p.trigger(u'a_channel', u'an_event', {u'some': u'data'})
        
        
#       self.bus.notify("set_game_mode", {"mode": 5 })
#       self.bus.notify("reset_score")
#       self.bus.notify("set_players",{'black':['Nils','Max'], 'yellow':['Arlington','Keith']})
