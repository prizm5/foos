
import config
import os
from subprocess import call

class Plugin:
    def __init__(self, bus):
        
    def run(self):
        call(["web/startserver.sh",config.web_folder,config.server_port])
