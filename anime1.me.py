
import pyautogui
from selenium import webdriver
from time import sleep

screen_x, screen_y = pyautogui.size()
tab1_x = 203
tab1_y = 22
tab2_x = 509
tab2_y = 21
ab_x = 395
ab_y = 68
save_x = 1054
save_y = 160
next_x = 258
next_y = 919
play_x = 631
play_y = 622
url_x = 877
url_y = 784

for i in range(0, 1):
	pyautogui.moveTo(play_x, play_y, duration = 1)
	pyautogui.click()
	pyautogui.press('f12')
	sleep(1)
	pyautogui.hotkey('ctrl', 'f')
	pyautogui.typewrite('mp4')
	pyautogui.moveTo(url_x, url_y, duration = 1)
	pyautogui.click(clicks = 2)
	pyautogui.hotkey('ctrl', 'c')


	pyautogui.moveTo(tab2_x, tab2_y, duration = 1)
	pyautogui.click()

	pyautogui.moveTo(ab_x, ab_y, duration = 1)
	pyautogui.click()
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')
	sleep(10)

	pyautogui.moveTo(screen_x/2, screen_y/2, duration = 1)
	pyautogui.click(button = 'right')
	pyautogui.moveTo(save_x, save_y, duration = 1)
	pyautogui.click()
	sleep(10)
	pyautogui.press('enter')

	pyautogui.moveTo(tab1_x, tab1_y, duration = 1)
	pyautogui.click()
	pyautogui.press('f12')
	pyautogui.moveTo(next_x, next_y, duration = 1)
	pyautogui.click()
	sleep(3)

pyautogui.alert(text = 'Finished', button = 'OK')