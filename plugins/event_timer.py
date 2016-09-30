#!/usr/bin/python3

import time
import queue
from threading import Thread
import config
import logging.config
import json
import requests
import schedule

logging.config.dictConfig(config.log)
logger = logging.getLogger(__name__)

CLIENT_SECRETS_FILE = "client_secrets.json"


class Plugin():
    def __init__(self, bus):
        self.bus = bus
        self.sched = Scheduler()
        self.sched.start()
        schedule.every().day.at("12:55").do(job_function)

    def run(self):
        while True:
            # Do other things in the meantime here...
            schedule.run_pending()
            time.sleep(1)
        
    def job_function():
        self.bus.notify('sudden_death')