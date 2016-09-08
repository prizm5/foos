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
        
        self.greenpush = 0
        self.game_mode = GameState.Idle

    def process_event(self, ev):
        now = time.time()
        if ev.name == "set_game_mode":
            self.game_mode = GameState.Active
        if ev.name == "score_reset":
            self.game_mode = GameState.Idle

    def run(self):
        while True:
            time.sleep(0.01)
    
    def handle_yellow(self, channel):
        self.bus.notify('goal_event', {'source': 'serial', 'team': 'yellow', 'duration': 100001})
        
    def handle_black(self, channel):
        self.bus.notify('goal_event', {'source': 'serial', 'team': 'black', 'duration': 100001})
    
    def handle_red_button(self, channel):
        self.bus.notify("set_game_mode", {"mode": 10 })
        self.bus.notify("reset_score")
        self.bus.notify("set_players",{'black':['Player 1','Player 2'], 'yellow':['Player 3','Player 4']})
        # start = {
        #         "black":["Player 1","Player 2"], 
        #         "yellow":["Player 3","Player 4"],
        #         "mode": 10,
        #         "stations": [ { "name": "Faiz", "station": "Secane" },
        #                       { "name": "Nilhouse", "station": "Gladstone" } ]
        #         } 
        # self.bus.notify("start_game",start )
        
    def handle_green_button(self, channel):
        if self.game_mode == GameState.Active and self.greenpush == 1 :
           self.bus.notify('goal_event', {'source': 'serial', 'team': 'yellow', 'duration': 100001})
           self.greenpush += 1 
        else:
            self.greenpush = 0


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
