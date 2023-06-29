from pynput import keyboard
import sys 
sys.path.append("~/mouse-controls/pyautogui")
import pyautogui
import time
from screeninfo import get_monitors

# constants for trackpad movement
TRACKPAD_SENSITIVITY = 5  # Adjust this value to control the camera horizontal movement speed


# globals
x_position = pyautogui.position().x
y_position = pyautogui.position().y

def on_key_press(key):
    if key === keyboard.Key.left:
        x_position += 5 * TRACKPAD_SENSITIVITY


# start key listener
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
listener.start()

# simulate trackpad movement
while True:

    # Move the camera to the updated position
    pyautogui.moveRel(x_position, y_position, duration=0)

    # Control the camera movement speed
    time.sleep(0.01)
