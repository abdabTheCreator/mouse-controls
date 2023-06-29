import pyautogui
import sys 
sys.path.append("~/mouse-controls/pyautogui")
import time

# Define the duration of each pan movement
pan_duration = 0.5

# Simulate camera pan from up to down
pyautogui.keyDown('w')
time.sleep(pan_duration)
pyautogui.keyUp('w')

# Simulate camera pan from left to right
pyautogui.keyDown('a')
time.sleep(pan_duration)
pyautogui.keyUp('a')

pyautogui.keyDown('d')
time.sleep(pan_duration)
pyautogui.keyUp('d')
