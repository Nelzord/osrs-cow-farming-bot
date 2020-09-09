import pyautogui
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

cycles = 0
delay = 2
button = Button.left
button2 = Button.right
activatorkey = KeyCode(char= 'a')
exitingkey = KeyCode(char= 'b')


class ClickMouse(threading.Thread) :
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
        while (self.program_running == True):
            while (self.running == True):
                loc = None
                cow1 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow1.png", confidence= .53)
                if cow1 is not None:
                    loc = cow1
                cow2 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow2.png", confidence= .53)
                if cow2 is not None:
                    loc = cow2
                cow3 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow3.png", confidence= .53)
                if cow3 is not None:
                    loc = cow3
                cow4 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow4.png", confidence= .53)
                if cow4 is not None:
                    loc = cow4
                cow5 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow5.png", confidence= .53)
                if cow5 is not None:
                    loc = cow5
                cow6 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow6.png", confidence= .53)
                if cow6 is not None:
                    loc = cow6
                cow7 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow7.png", confidence= .53)
                if cow7 is not None:
                    loc = cow7
                cow8 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow8.png", confidence= .53)
                if cow8 is not None:
                    loc = cow8
                cow9 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow9.png", confidence=.53)
                if cow9 is not None:
                    loc = cow9
                cow10 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow10.png", confidence=.53)
                if cow10 is not None:
                    loc = cow10
                cow11 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow11.png", confidence=.53)
                if cow11 is not None:
                    loc = cow11
                cow12 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow12.png", confidence=.53)
                if cow12 is not None:
                    loc = cow12
                cow13 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow13.png", confidence=.53)
                if cow13 is not None:
                    loc = cow13
                cow14 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow14.png", confidence=.53)
                if cow14 is not None:
                    loc = cow14
                cow15 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow15.png", confidence=.53)
                if cow15 is not None:
                    loc = cow15
                cow16 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow16 is not None:
                    loc = cow16
                cow17 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow17 is not None:
                    loc = cow17
                cow18 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow18 is not None:
                    loc = cow18
                cow19 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow19 is not None:
                    loc = cow19
                cow20 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow20 is not None:
                    loc = cow20
                cow21 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow21 is not None:
                    loc = cow21
                cow22 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow22 is not None:
                    loc = cow22
                cow23 = pyautogui.locateOnScreen(r"C:\Users\Julie\PycharmProjects\MinerBot\cow16.png", confidence=.53)
                if cow23 is not None:
                    loc = cow23
                if loc is not None:
                    print(pyautogui.center(loc))
                    pyautogui.moveTo(pyautogui.center(loc));
                    mouse.click(self.button)
                    time.sleep(5)
                time.sleep(.2)

time.sleep(1.5)
mouse = Controller()
click_thread = ClickMouse(delay, button)
orelocation = pyautogui.position()
click_thread.start()


def on_press(key):
    if key == activatorkey:
        if (click_thread.running == True):
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exitingkey:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()