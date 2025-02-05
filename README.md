# Stop Following
* Bot to Stop following people you don`t want to follow more.

### Step by Step

* First of all you need to do this:
```
pip install pyautogui
```

* You need to import this two libraries -
```
import pyautogui
import time
```

* Two variables, X and Y, are the pixel i need to click on my screen
```
time.sleep(5)

x = 1100
y = 465

following = 61 #put your number of following
```

* A while loop for my actions, here i go to the "following" button and i click, after this, i go to the "stop following" and i confirm clicking there.
* After i stop to following somebody i scroll 72 pixels, and the next person will be the first on my list.
* After every action, you need to give time to your cursor move.
```
while(following > 0):
    for i in range(following):
        
        pyautogui.moveTo(x, y) #following button
        time.sleep(0.3)
        pyautogui.click() #click on the button

        time.sleep(0.3)
        pyautogui.moveTo(950, 655) #stop following button
        pyautogui.click() #click on the button

        time.sleep(0.3)
        pyautogui.scroll(-72) #scroll the list
        time.sleep(0.3)
```

*If you need some help, send me a message*
- [LinkedIn](https://www.linkedin.com/in/nata-batista)
