
import config
import os
from subprocess import call
import SimpleHTTPServer
import SocketServer
import config

class Plugin:
    def __init__(self, bus):
        call(["web/startserver.sh",config.web_folder,config.server_port])
