onscreen_leds_enabled = False
standby_timeout_secs = 600
bg_change_secs = 300
bg_amount = 100
hipchat_token = 'your_token'
hipchat_room = 'your_room_id'

pusher_channel ='foosball'
pusher_channel_out ='foosball-out'

min_goal_usecs = 1000
min_secs_between_goals = 0

button_debnce=500
red_button=27
green_button=17
yellow_trigger=23
black_trigger=24

server_port='8000'
web_folder='web'

# dev set

plugins = ['pusherclient', 'game', 'score', 'physical', 'control', 'sound', 'goalpic','event_timer']

# full blown set: arduino, camera, league & sync, upload, chat
# plugins = ['replay', 'camera', 'score', 'game', 'upload', 'sound', 'leds', 'io_debug', 'io_serial', 'standby', 'menu', 'control', 'hipbot', 'motiondetector', 'league', 'event_debugger', 'league_sync']

show_instructions = False

replay_path = '/home/pi/replay'
ignore_recent_chunks = 1
short_chunks = 10
long_chunks = 25

league_dir = './league'
league_url = 'http://localhost:8888/api'
league_apikey = 'put-your-apikey-here'

# config parameters for motion detector
# MV frame size
md_size = (82, 46)
# crop pixels on each size of the frame to avoid detecting movement outside of the table
md_crop_x = 25
# threshold to consider MV movement
md_mv_threshold = 100000
# number of vectors to consider frame to contain movement
md_min_vectors = 30
# number of contiguous frames to required to consider it movemen
md_min_frames = 9

# send people_stop_playing event after X seconds without movement
md_ev_absence_timeout = 30
# send movement_detected every X seconds
md_ev_interval = 2

log = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(levelname)6s %(name)s - %(message)s",
            "datefmt": "%H:%M:%S"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "stream": "ext://sys.stdout"
        },

        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "/home/pi/event.log",
            "maxBytes": 1000000,
            "backupCount": 3
        },
    },

    "loggers": {
        "plugins.event_debugger": {
            "level": "DEBUG",
            "handlers": ["file_handler"],
            "propagate": "no",

        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    }
}
