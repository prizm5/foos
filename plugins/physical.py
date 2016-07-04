#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import queue
from threading import Thread


class Plugin():
    def __init__(self, bus):
        self.bus = bus
        self.bus.subscribe(self.process_event, thread=True)
        GPIO.setmode(GPIO.BCM)
        self.AddButton(17, self.handle_red_button,500)
        
        self.bus.notify("set_game_mode", {"mode": 5 })
        self.bus.notify("reset_score")
        self.bus.notify("set_players",{'black':['Nils','Max'], 'yellow':['Arlington','Keith']})
        

    def process_event(self, ev):
        now = time.time()

    def run(self):
        while True:
            time.sleep(0.01)
    
    def handle_red_button(self, channel):
        self.bus.notify('goal_event', {'source': 'serial', 'team': 'yellow', 'duration': 100001})
        #self.bus.notify('increment_score', {'team': 'yellow'})

    def AddSensor(self, port, callback, bounce):
        p = int(port)
        b = int(bounce)
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(p, GPIO.FALLING, callback=callback, bouncetime=b)

    def AddButton(self, port, callback, bounce):
        p = int(port)
        b = int(bounce)
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(p, GPIO.FALLING, callback=callback, bouncetime=b)
