# 🍅 Pomidor
Pomidor is a highly customizable Pomodoro technique timer implemented with python and Tkinter. 

### 💎 Goals and Roadmap
Tomato was created to provide a fresh, simple, and customizable Pomodoro timer for everyone in need.
1. Tomato should be built and constructed with availability in mind, able to run smoothly on all platforms. 
2. It should be as customizable as possible, including custom design themes, plugins, and other functionality.

### 🗺 Roadmap:
1. Create a timer with a simple config file for customizations.
2. Allow users to configure timer & sound effects through GUI.
3. Allow users to configure themes and styles through GUI.
4. Make the Tomato Pomodoro timer available to download through the terminal.
5. Create a landing page 
6. Create a plugin to run doom on this timer.

# 📂 Structure
1. main.py -> As of right now, all initialization happens inside this file.
2. timer_class.py -> This class iterates and keeps track of the timer in minutes and seconds.
3. window_class.py -> This class creates and updates the main root window.
4. images -> Contains images
5. sounds -> Contains sounds

# 📄 How to run
To run Pomidor timer - clone or download the repo and run main.py
```bash
$ git clone https://github.com/KonstantinBelenko/Pomidor.git
$ cd Pomidor

# Install dependencies
$ pip install -r requirements.txt

# Next thing you would want to do is to configure the app for yourself 
# Open the main.py and set the timing configuration and preferred styles
# After that - you can run it. 
$ python main.py
```
