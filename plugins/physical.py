import RPi.GPIO as GPIO
import time
import queue
from threading import Thread
from .buttons import *

class Plugin():
    def __init__(self, bus):
        self.bus = bus
        self.bus.subscribe(self.process_event, thread=True)
        AddButton(17, self.handle_red_button,500)

    def process_event(self, ev):
        now = time.time()
        if ev.name == "score_changed":

    def run(self):
        while True:
          while not self.queue.empty():
            ev = self.queue.get_nowait()
            self.process_event(ev)
          time.sleep(0.01)
    
    def handle_red_button(self, channel):
        self.logger.info("Red button pushed")
        if self.__state != GameState.idle:
            if self.__state == GameState.live_game:
                self.messages.send_game_queued(self.game.id)
            self.__state = GameState.idle

    def team1Scored(self):
      self.bus.notify('black_minus')

    def AddSensor(self, port, callback, bounce):
        p = int(port)
        b = int(bounce)
        self.logger.info("Sensor added: Port: %s | Callback: %s | Bounce: %s", p, callback, b)
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(p, GPIO.FALLING, callback=callback, bouncetime=b)

    def AddButton(self, port, callback, bounce):
        p = int(port)
        b = int(bounce)
        self.logger.info("Button added: Port: %s | Callback: %s | Bounce: %s", p, callback, b)
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(p, GPIO.FALLING, callback=callback, bouncetime=b)