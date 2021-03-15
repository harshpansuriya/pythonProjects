import pyautogui
import time

message = 5 #How many times you want to send your message.

while message > 0:
    time.sleep(4)
    pyautogui.typewrite("Like video") #This is your Message
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1

    #Let's run it.

    #work very beutifully. 

    #Thank you for Watching..