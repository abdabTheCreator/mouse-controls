import sys 
sys.path.append("~/mouse-controls/pyautogui")
import pyautogui
import time


# Define the duration of each pan movement
pan_duration = 0.5

# Define the distance and direction of camera pan
pan_distance_x = 100  # Adjust the value as needed for horizontal panning
pan_distance_y = 100  # Adjust the value as needed for vertical panning

# Simulate camera pan from up to down
pyautogui.moveRel(0, -pan_distance_y, duration=pan_duration)

# Simulate camera pan from left to right
pyautogui.moveRel(-pan_distance_x, 0, duration=pan_duration)
pyautogui.moveRel(pan_distance_x, 0, duration=pan_duration)
