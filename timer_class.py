from playsound import playsound

class Timer:
    """
    Timer class is used to monitor pomodoro time, events and phases.
    
    ---
    It holds information about the current state of the timer in minutes and seconds.
    It also holds information about the current phase and all phases in general.
    This class is also used to play sound on timer end.

    ---
    Attributes:
        phases:dict                 | A dictionary mapping of phases, their names and how much time each of them take.
        alarm_sound_file_path: str  | String path to an audio file to be played when the timer ends.
    """

    def __init__(self, phases:dict, alarm_sound_file_path:str):
        """
        This function initializes the timer class.

        ---
        Args:
            phases:dict | A dictionary mapping of phases, their names and how much time each of them take.
            alarm_sound_file_path: str | String path to an audio file to be played when the timer ends.

        ---
        Returns: None
        """

        self.minutes = phases["main"]["minutes"]
        self.seconds = phases["main"]["seconds"]
        
        self.pomodoro_time    = (phases["main"]["minutes"], phases["main"]["seconds"])
        self.short_break_time = (phases["short"]["minutes"], phases["short"]["seconds"])
        self.long_break_time  = (phases["long"]["minutes"], phases["long"]["seconds"])
 
        self.alarm_sound_file_path = alarm_sound_file_path

        self.phases_dict = phases
        self.phase       = list(phases.keys())[0]

    def get_time(self) -> str:
        """
        This function formats and returns the current time in minutes and seconds.

        ---
        Args: None

        ---
        Returns:
            str: Current time in format 00:00
        """
        minutes = str(self.minutes)
        seconds = str(self.seconds)

        if len(minutes) == 1:
            minutes = "0" + minutes
        if len(seconds) == 1:    
            seconds = "0" + seconds

        return "{0}:{1}".format(minutes, seconds)

    def set_time(self, minutes:int = 0, seconds:int = 0) -> None:
        """
        This function sets current time to the provided time.

        ---
        Args:
            `minutes:int = 0` | Time in minutes
            `seconds:int = 0` | Time in seconds

        ---
        Returns: None
        """
        self.minutes = minutes
        self.seconds = seconds

    def play_alarm(self, path:str = None) -> None:
        """
        Plays an audiofile specified by path. If the path is not specified or None, will play the default alarm sound.

        ---
        Args:
            `path:str = None` | The path to the audio file to be played.
            Example -> './sounds/alarm.mp3'

        ---
        Returns: None
        """
        if not path: path = self.alarm_sound_file_path
        playsound(path)

    def shift(self) -> str:
        """
        Shifts the current pomodoro phase. Phases are specified by the self.phases_list dictionary.

        ---
        Args: None

        ---
        Returns:
            str: Phase name
        """
        list_of_keys = list(self.phases_dict.keys())

        # If the current phase is the last one, the next phasae should be the first one
        if self.phase == list_of_keys[-1]:
            self.phase = list_of_keys[0]
        
        # Else, just select the next phase
        else:
            self.phase = list_of_keys[list_of_keys.index(self.phase)+1]

        self.minutes = self.phases_dict[self.phase]["minutes"]
        self.seconds = self.phases_dict[self.phase]["seconds"]

        return self.phases_dict[self.phase]['name']

    def get_current_phase(self):
        """
        Returns current phase

        ---
        Args: None

        ---
        Returns:
            str: Current phase name
        """
        return self.phases_dict[self.phase]['name']

    def decrease(self) -> bool:
        """
        Decreases time counter by one second. It will automatically change minute and second
        counter and not go down into the negative.

        ---
        Args: None

        ---
        Returns:
            bool: Returns True by default, False if the timer has ran down to 00:00
        """
        minutes = self.minutes
        seconds = self.seconds

        if seconds == 0 and minutes == 0:
            return False
        
        if seconds == 0:
            minutes -= 1
            seconds = 60
        
        seconds -= 1

        self.minutes = minutes
        self.seconds = seconds

        return True

