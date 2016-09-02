
import config
import os
from subprocess import call

class Plugin:
    def __init__(self, bus):
        a=1
        
    def run(self):
        call("chromium-browser http://localhost:8000/web", shell=True)
