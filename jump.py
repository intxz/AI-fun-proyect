import pyautogui
import time

def jump():
    pyautogui.press('space')

# Test jumping
time.sleep(2)  # Wait before starting
while True:
    jump()
