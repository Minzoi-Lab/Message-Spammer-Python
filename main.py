import pyautogui
import time
import pyperclip
import keyboard

message = input("What message do you want to spam?: ")
delay = float(input("How many seconds between each message? (Recommended: 0.5): "))
amount = int(input("How many times do you want to send the message? (0 = infinite): "))
time = int(input("Finally, how much seconds do you need to click on the textbox?")
pyperclip.copy(message)

print(f"You have {time} seconds to click the chat box...")
print("Press Ctrl+D at any time to stop.")
time.sleep(time)

sent = 0

while amount == 0 or sent < amount:
    if keyboard.is_pressed("ctrl+d"):
        break

    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    sent += 1

    if keyboard.wait("ctrl+d", delay) == "ctrl+d":
        break

print("done.")
