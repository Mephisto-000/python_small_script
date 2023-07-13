import os
import time
import pyautogui


def mouse_position_check():
    while True:
        position = pyautogui.position()
        os.system("clear")
        print(f"X : {position[0]}, Y : {position[1]}")
        time.sleep(0.3)


def screem_size_check():
    print(f"screem size : (X:{pyautogui.size()[0]}, Y:{pyautogui.size()[1]})")


# (0,0)       X -->
# +---------------------------+
# |                           |  Y
# |                           |  |
# |   width x height screen   |  |
# |                           |  V
# |                           |
# |                           |
# +---------------------------+ (X, Y)
