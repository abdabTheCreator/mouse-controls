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
    if key == 'up':
        pyautogui.moveRel(0, -pan_distance_y, duration=pan_duration)
    elif key == 'down':
        pyautogui.moveRel(0, pan_distance_y, duration=pan_duration)
    elif key == 'left':
        pyautogui.moveRel(-pan_distance_x, 0, duration=pan_duration)
    elif key == 'right':
        pyautogui.moveRel(pan_distance_x, 0, duration=pan_duration)

# Monitor keyboard input for arrow keys
while True:
    if keyboard.is_pressed('up'):
        simulate_pan('up')
    elif keyboard.is_pressed('down'):
        simulate_pan('down')
    elif keyboard.is_pressed('left'):
        simulate_pan('left')
    elif keyboard.is_pressed('right'):
        simulate_pan('right')
    time.sleep(0.1)  # Adjust the sleep time as needed
