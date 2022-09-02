from timer_class import Timer
from window_class import Window

# Configuration variables
alarm_sound_file_path = "./sounds/alarm.mp3"
phases = {
    "main": {
        "name": "Pomodoro",
        "minutes": 25,
        "seconds": 0
    }, 

    "short": {
        "name": "Short Break",
        "minutes": 15,
        "seconds": 0
    },

    "long": {
        "name": "Long Break",
        "minutes": 30,
        "seconds": 0
    }  
}

window_style = {
    "bg": "#151515",
    "fg": "#ffffff"
}

# Initialize the timer with default time settings
timer = Timer(
    phases                = phases,
    alarm_sound_file_path = alarm_sound_file_path,
)

window = Window(
    size            = (500, 500),
    timer           = timer,
    title           = "Pomodoro Timer",
    style           = window_style,
    pause_after_end = False
)