import pyautogui
import time

# x always 1100
# y always +72

time.sleep(5)

x = 1100
y = 465

following = 61 #put your number of following

pyautogui.moveTo(1100, 465)

while(following > 0):
    for i in range(following):
        
        pyautogui.moveTo(1100, 465) #following button
        time.sleep(0.3)
        pyautogui.click() #click on the button

        time.sleep(0.3)
        pyautogui.moveTo(950, 655) #stop following button
        pyautogui.click() #click on the button

        time.sleep(0.3)
        pyautogui.scroll(-72) #scroll the list
        time.sleep(0.3)
