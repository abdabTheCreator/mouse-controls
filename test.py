import sys 
sys.path.append("~/mouse-controls/pyautogui")
import pyautogui
import time
from pynput import keyboard
# Define the duration of each pan movement
pan_duration = 0.5

# Define the distance and direction of camera pan
pan_distance_x = 100  # Adjust the value as needed for horizontal panning
pan_distance_y = 100  # Adjust the value as needed for vertical panning

# Function to simulate camera pan
def simulate_pan(key):
    if key == keyboard.Key.up:
        pyautogui.moveRel(0, -pan_distance_y, duration=pan_duration)
    elif key == keyboard.Key.down:
        pyautogui.moveRel(0, pan_distance_y, duration=pan_duration)
    elif key == keyboard.Key.left:
        pyautogui.moveRel(-pan_distance_x, 0, duration=pan_duration)
    elif key == keyboard.Key.right:
        pyautogui.moveRel(pan_distance_x, 0, duration=pan_duration)

# Define the callback for key press event
def on_key_press(key):
    simulate_pan(key)

# Define the callback for key release event (if needed)
def on_key_release(key):
    pass

# Create listener objects
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
