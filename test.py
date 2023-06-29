import sys 
sys.path.append("~/mouse-controls/pyautogui")
import pyautogui
import time

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
    key = pyautogui.keyDown()
    if key == 'up' or key == 'down' or key == 'left' or key == 'right':
        simulate_pan(key)
    time.sleep(0.1)  # Adjust the sleep time as needed
