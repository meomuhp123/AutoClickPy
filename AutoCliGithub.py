import os

os.system("pip install pyautogui")
os.system("pip install opencv-python")

import pyautogui
import time


def AutoCli(prm):	
  loop = prm
  while loop == 1:
    try:
      x, y = pyautogui.locateCenterOnScreen("img.png", confidence=0.8)
    except:
      print("error")
      Main()
    else:
      pyautogui.click()

def Main():
  time.sleep(3)
  try:
    x, y = pyautogui.locateCenterOnScreen("img.png", confidence=0.8)
    pyautogui.moveTo(x, y, 1)
  except:
    print("error")
    Main()
  else:
    AutoCli(1)

Main()