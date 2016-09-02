
import config
import os
from subprocess import call

class Plugin:
    def __init__(self, bus):
        
    def run(self):
        call("chromium-browser http://localhost:8000/web",config.web_folder,config.server_port], shell=True)
