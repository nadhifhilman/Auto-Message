import pyautogui
import keyboard
import time

print("automasi aan mulai dalam waktu 5 detik")
time.sleep(5)

while keyboard.is_pressed("c") == False:
    # pyscreeze.locate(x, y)
    pyautogui.click(x = 701, y = 98)
    
    pyautogui.typewrite(
        "hari", 
        interval=0.05
    )
    time.sleep(1)  # tunggu 1 detik
    pyautogui.press("enter")    

    