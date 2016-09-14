import config
import os
from subprocess import call


class Plugin:
    def __init__(self, bus):
        self.bus = bus
        bus.subscribe_map( 'score_goal': lambda d: self.snap()}, thread=True)

    def snap(self):
        call(["video/capture.sh"])
        self.bus.notify('picture_captured')
