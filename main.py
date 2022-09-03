from timer_class import Timer
from window_class import Window

# Configuration variables
alarm_sound_file_path = "./sounds/alarm.mp3"
pause_after_end = True
phases = {
    "main": {
        "name": "Pomodoro",
        "minutes": 0,
        "seconds": 25
    }, 

    "short": {
        "name": "Short Break",
        "minutes": 0,
        "seconds": 15
    },

    "long": {
        "name": "Long Break",
        "minutes": 0,
        "seconds": 30
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
    pause_after_end = pause_after_end
)