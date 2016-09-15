import config
import os
from subprocess import call


class Plugin:
    def __init__(self, bus):
        self.bus = bus
        fmap = {'score_goal': lambda d: self.snap()}
        self.bus.subscribe_map(fmap, thread=True)

    def snap(self):
	call("video/capture.sh")
        self.bus.notify('picture_captured')
