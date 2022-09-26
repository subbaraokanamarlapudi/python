import time,pyautogui
msg = input("Enter your message:")
n = input("How many times?: ")
time.sleep(10)
for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n') 
   