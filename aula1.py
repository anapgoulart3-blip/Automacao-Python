import pyautogui as pa
import time

pa.Pause=1
pa.press ('win')
pa.write('Microsoft Edge')
pa.press('Enter')
time.sleep (3)
pa.write('youtube.com')
pa.press ('Enter')