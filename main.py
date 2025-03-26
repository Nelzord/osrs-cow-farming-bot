import pyautogui
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os

# Configuration
cycles = 0
delay = 2
button = Button.left
button2 = Button.right
activatorkey = KeyCode(char='a')
exitingkey = KeyCode(char='b')
confidence_level = 0.53
photos_folder = os.path.join(os.path.dirname(__file__), "photos")

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.cycles = cycles
        self.delay = delay
        self.button = button
        self.button2 = button2
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        global loc
        while self.program_running:
            while self.running:
                loc = None
                # Loop through all image files in the photos folder
                for image_file in os.listdir(photos_folder):
                    if image_file.endswith(".png"):
                        image_path = os.path.join(photos_folder, image_file)
                        loc = pyautogui.locateOnScreen(image_path, confidence=confidence_level)
                        if loc is not None:
                            break  # Stop searching once a match is found

                if loc is not None:
                    center = pyautogui.center(loc)
                    print(center)
                    pyautogui.moveTo(center)
                    mouse.click(self.button)
                    time.sleep(5)
                time.sleep(0.2)

time.sleep(1.5)
mouse = Controller()
click_thread = ClickMouse(delay, button)
orelocation = pyautogui.position()
click_thread.start()

def on_press(key):
    if key == activatorkey:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exitingkey:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()