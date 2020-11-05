import pyautogui, time
a = int(input("Enter the number of msg you want to send: "))
time.sleep(4)
while a>0:
    pyautogui.typewrite("😂")
    pyautogui.press("enter")
    a = a-1