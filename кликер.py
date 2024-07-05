import keyboard
import mouse
import time 

print("alt+z")
isClicking = False

def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Выключили")
    else:
        isClicking = True
        print ("Включили")


keyboard.add_hotkey('Alt + Z', set_clicker)

while True:
    if isClicking:
        mouse.double_click(button = 'left')
        time.sleep(0.01)
