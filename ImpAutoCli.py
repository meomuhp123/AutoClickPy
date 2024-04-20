import pyautogui
import time


def AutoCli(prm):	
	loop = prm
	while loop == 1:
		try:
			x, y = pyautogui.locateCenterOnScreen("img.png", confidence=0.8)
		except:
			print("Đối tượng không còn tồn tại")
			Main()
		else:
			pyautogui.click()

def Main():
	time.sleep(3)
	try:
		x, y = pyautogui.locateCenterOnScreen("img.png", confidence=0.8)
		pyautogui.moveTo(x, y, 1)
	except:
		print("Không tìm thấy đối tượng trùng khớp")
		Main()
	else:
		AutoCli(1)

Main()