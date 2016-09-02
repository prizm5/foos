
import config
import os
from subprocess import call

class Plugin:
    def __init__(self, bus):
        a=1
        
    def run(self):
        call("python -m SimpleHTTPServer " + config.server_port , shell=True)
