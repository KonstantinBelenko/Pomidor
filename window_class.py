import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
from timer_class import Timer


class Window:
    """
    Window class is used to display Pomidor pomodoro timer in conjunction with the timer class.

    It creates a window and runs a main loop to update and display the timer.

    ---
    Attributes:
        size:tuple | width and height of the window.
        timer:Timer | Timer class instance.
        title:str | Window title.
        style:dict | Style dictionary for the window.
    """

    def __init__(self, size:tuple, timer:Timer, title:str, style:dict, pause_after_end:bool = True) -> None:
        """
        This function initializes the window class. It accepts a few parameters to initialize it.

        It creates the window and text / button components. Automatically moves the window to the center
        of the screen. It also starts the timer and runs the __refresh() function inside the loop, repeating
        it each second.

        Args:
            size:tuple | Width and height of the window.
            timer:Timer | Timer class instance.
            style:dict | Style dictionary for the window.
            pause_after_end:bool = True | To pause the timer after it runs down to 00:00 or to 
            start the next phase automatically.
        """
        
        # Set the settings
        self.style = style
        self.window = tk.Tk()
        self.window.title()
        self.window.title(title)

        self.pause_after_end = pause_after_end
        self.timer = timer

        self.window.configure(width=size[0], height=size[1])
        self.window.resizable(False, False)
        self.window.pack_propagate(False)
        self.window.configure(bg=self.style['bg'])
        self.window.iconbitmap("./images/favicon.ico")

        # Move window center
        winWidth = self.window.winfo_reqwidth()
        winwHeight = self.window.winfo_reqheight()
        posRight = int(self.window.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(self.window.winfo_screenheight() / 2 - winwHeight / 2)
        self.window.geometry("+{}+{}".format(posRight, posDown))

        # Phase label
        self.phase_var = tk.StringVar()
        self.phase_var.set(timer.get_current_phase())

        self.phase_label = tk.Label(self.window, textvariable=self.phase_var)
        self.phase_label.config(font=("Poppins", 28), bg=self.style['bg'], fg=self.style['fg'])
        self.phase_label.pack(ipadx=5, ipady=2, expand=True)

        # Timer
        self.is_running = tk.BooleanVar()
        self.is_running.set(False)

        self.time_var = tk.StringVar()
        self.time_var.set(self.timer.get_time())

        self.button_name = tk.StringVar()
        self.button_name.set("Start")

        self.time_label = tk.Label(self.window, textvariable=self.time_var)
        self.time_label.config(font=("Poppins", 32), bg=self.style['bg'], fg=self.style['fg'])
        self.time_label.pack(ipadx=5, ipady=2, expand=True)

        self.start_button = tk.ttk.Button(
            self.window,
            textvariable=self.button_name,
            command=self.__pause,
        ).pack(ipadx=5, ipady=2, expand=True)

        self.__refresh()
        self.window.mainloop()

    def __pause(self):
        """
        This function pauses the timer and the __refresh function. Stops the timer class from counting.
        
        It automatically flips the timer by changine the self.is_running variable.

        ---
        Args: None

        ---
        Returns: None
        """

        if self.is_running.get() == True:
            self.is_running.set(False)
            self.button_name.set("Start")
        else:
            self.is_running.set(True)
            self.button_name.set("Stop")
            self.__refresh()

    def __refresh(self):
        """
        This function refreshes the timer and keeps track of the time and triggers.
        
        It will run the audio alarm when the timer runs down to 00:00 and automatically
        changes the current phase.

        ---
        Args: None

        ---
        Returns: None
        """
        if self.is_running.get():

            ended = self.timer.decrease()
            self.time_var.set(self.timer.get_time())

            # If the timer has ended --> 00:00
            if ended == False:

                # Pause the timer
                if self.pause_after_end: 
                    self.__pause()

                # Play the alarm sound
                self.timer.play_alarm()

                # Shift the phase to either work or rest
                self.phase_var.set( self.timer.shift() )

                # Update the clock
                self.time_var.set(self.timer.get_time())

            self.window.after(1000, self.__refresh)