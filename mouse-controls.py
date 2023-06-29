from pynput import keyboard
import sys 
sys.path.append("~/mouse-controls/pyautogui")
import pyautogui

# constants for trackpad movement
TRACKPAD_SENSITIVITY = 5  # Adjust this value to control the camera movement speed

# globals
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

# handle arrow key presses
def on_key_press(key):
    global left_pressed, right_pressed, up_pressed, down_pressed

    if key == keyboard.Key.left:
        left_pressed = True
    elif key == keyboard.Key.right:
        right_pressed = True
    elif key == keyboard.Key.up:
        up_pressed = True
    elif key == keyboard.Key.down:
        down_pressed = True

# handle arrow key releases
def on_key_release(key):
    global left_pressed, right_pressed, up_pressed, down_pressed

    if key == keyboard.Key.left:
        left_pressed = False
    elif key == keyboard.Key.right:
        right_pressed = False
    elif key == keyboard.Key.up:
        up_pressed = False
    elif key == keyboard.Key.down:
        down_pressed = False

# start key listener
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
listener.start()

# simulate trackpad movement
while True:
    # simulate trackpad movement based on arrow key presses
    x_move = (right_pressed - left_pressed) * TRACKPAD_SENSITIVITY
    y_move = (down_pressed - up_pressed) * TRACKPAD_SENSITIVITY
    pyautogui.move(x_move, y_move, duration=0)

    # to control the camera movement speed
    time.sleep(0.01)
