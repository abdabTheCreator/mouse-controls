from pynput import keyboard
import sys 
sys.path.append("~/mouse-controls/pyautogui")
import pyautogui
import time
from screeninfo import get_monitors

# constants for trackpad movement
TRACKPAD_SENSITIVITY_X = 5  # Adjust this value to control the camera horizontal movement speed
TRACKPAD_SENSITIVITY_Y = 5  # Adjust this value to control the camera vertical movement speed

# globals
x_position = pyautogui.position().x
y_position = pyautogui.position().y
x_move = 0
y_move = 0

# Screen bounds
screen_width, screen_height = get_monitors()[0].width, get_monitors()[0].height

# handle arrow key presses
def on_key_press(key):
    global x_move, y_move

    if key == keyboard.Key.left:
        x_move = -TRACKPAD_SENSITIVITY_X
    elif key == keyboard.Key.right:
        x_move = TRACKPAD_SENSITIVITY_X
    elif key == keyboard.Key.up:
        y_move = -TRACKPAD_SENSITIVITY_Y
    elif key == keyboard.Key.down:
        y_move = TRACKPAD_SENSITIVITY_Y

# handle arrow key releases
def on_key_release(key):
    global x_move, y_move

    if key == keyboard.Key.left and x_move < 0:
        x_move = 0
    elif key == keyboard.Key.right and x_move > 0:
        x_move = 0
    elif key == keyboard.Key.up and y_move < 0:
        y_move = 0
    elif key == keyboard.Key.down and y_move > 0:
        y_move = 0

# start key listener
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
listener.start()

# simulate trackpad movement
while True:
    # Update the camera position based on the movement
    x_position += x_move
    y_position += y_move

    # Perform boundary checks
    x_position = max(0, min(x_position, screen_width))
    y_position = max(0, min(y_position, screen_height))

    # Move the camera to the updated position
    pyautogui.moveTo(x_position, y_position, duration=0)

    # Control the camera movement speed
    time.sleep(0.01)

from screeninfo import get_monitors

# constants for trackpad movement
TRACKPAD_SENSITIVITY_X = 5  # Adjust this value to control the camera horizontal movement speed
TRACKPAD_SENSITIVITY_Y = 5  # Adjust this value to control the camera vertical movement speed

# globals
x_position = pyautogui.position().x
y_position = pyautogui.position().y
x_move = 0
y_move = 0

# Screen bounds
screen_width, screen_height = get_monitors()[0].width, get_monitors()[0].height

# handle arrow key presses
def on_key_press(key):
    global x_move, y_move

    if key == keyboard.Key.left:
        x_move = -TRACKPAD_SENSITIVITY_X
    elif key == keyboard.Key.right:
        x_move = TRACKPAD_SENSITIVITY_X
    elif key == keyboard.Key.up:
        y_move = -TRACKPAD_SENSITIVITY_Y
    elif key == keyboard.Key.down:
        y_move = TRACKPAD_SENSITIVITY_Y

# handle arrow key releases
def on_key_release(key):
    global x_move, y_move

    if key == keyboard.Key.left and x_move < 0:
        x_move = 0
    elif key == keyboard.Key.right and x_move > 0:
        x_move = 0
    elif key == keyboard.Key.up and y_move < 0:
        y_move = 0
    elif key == keyboard.Key.down and y_move > 0:
        y_move = 0

# start key listener
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
listener.start()

# simulate trackpad movement
while True:
    # Update the camera position based on the movement
    x_position += x_move
    y_position += y_move

    # Perform boundary checks
    x_position = max(0, min(x_position, screen_width))
    y_position = max(0, min(y_position, screen_height))

    # Move the camera to the updated position
    pyautogui.moveTo(x_position, y_position, duration=0)

    # Control the camera movement speed
    time.sleep(0.01)
