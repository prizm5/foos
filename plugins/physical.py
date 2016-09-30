#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import queue
import config
from threading import Thread

class GameState:
    Idle, Active = range(2)
    
class Plugin():

    def __init__(self, bus):
        self.bus = bus
        self.bus.subscribe(self.process_event, thread=True)
        GPIO.setmode(GPIO.BCM)
        
        self.AddButton(config.red_button, self.handle_red_button, config.button_debnce)
        self.AddButton(config.green_button, self.handle_green_button, config.button_debnce)
        
        self.AddSensor(config.yellow_trigger, self.handle_yellow, config.button_debnce)
        self.AddSensor(config.black_trigger, self.handle_black, config.button_debnce)


    def process_event(self, ev):
        now = time.time()
        if ev.name == "score_reset":
            self.last_goal = None 

    def run(self):
        while True:
            time.sleep(0.01)
    
    def handle_yellow(self, channel):
        self.last_goal = 'yellow'
        self.bus.notify('goal_event', {'source': 'serial', 'team': 'yellow', 'duration': 100001})
        
    def handle_black(self, channel):
        self.last_goal = 'black'
        self.bus.notify('goal_event', {'source': 'serial', 'team': 'black', 'duration': 100001})
    
    def handle_red_button(self, channel):
        if self.last_goal != None:
            self.bus.notify('decrement_score', {'team': self.last_goal})

    def handle_green_button(self, channel):
        self.bus.notify("set_game_mode", {"mode": 10 })
        self.bus.notify("reset_score")
        self.bus.notify("set_players",{'black':[{'name':'Player 1','station':'Gladstone'}, {'name':'Player 2','station':'Queen Lane'}], 
                                      'yellow':[{'name':'Player 3','station':'Strafford'}, {'name':'Player 4','station':'Penllyn'}]})


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
