import config
import os
from subprocess import call


class Plugin:
    def __init__(self, bus):
        self.bus = bus
        bus.subscribe_map( 'score_goal': lambda d: self.snap()}, thread=True)

    def snap(self):
        call(["video/capture.sh", os.path.join(config.replay_path, "replay_{}.h264".format(replay_type))])
        # self.bus.notify('replay_start', extra)
        # call(["video/replay.sh", os.path.join(config.replay_path, "replay_{}.h264".format(replay_type))])
        # self.bus.notify('replay_end')
