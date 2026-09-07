import pyautogui
import time
import pyperclip

print("You have 10 seconds to open the right chat! if you want to turn it off press ctrl+c" 
)
time.sleep(10) 


i = 1


while True:
    text = f"haha you are getting spammed! {i}"
    pyperclip.copy(text)
    
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    
    i += 1  
    time.sleep(0.2)
