import time
from pynput import keyboard
from threading import Thread
from datetime import datetime
from logData import data

initialTime = datetime.strptime(data[0]["startAt"], "%M:%S:%f")
kbCtrl = keyboard.Controller()

def handleKey(keyCode: keyboard.KeyCode, startOffset: int, duration: int):
    time.sleep(startOffset)

    print(f"Press {keyCode} for {duration} seconds")
    
    kbCtrl.press(keyCode)
    
    time.sleep(duration)

    print(f"Release {keyCode}")
    
    kbCtrl.release(keyCode)

def start():
    for recordedData in data:
        if recordedData["key"] == "delete":
            continue

        keyCode = keyboard.Key.space if recordedData["key"] == "space" else keyboard.KeyCode(char=recordedData["key"])
        startAt = datetime.strptime(recordedData["startAt"], "%M:%S:%f")
        endAt = datetime.strptime(recordedData["endAt"], "%M:%S:%f")

        # Since all presses are queued at once, we offset subsequent keypresses
        # key startAt - processStartAt (first key press)
        startOffset = (startAt - initialTime).total_seconds()
        duration = (endAt - startAt).total_seconds()

        print(f"Key: {keyCode.char} | startOffset: {startOffset} | duration: {duration}")
        
        t = Thread(target=handleKey, args=[keyCode, startOffset, duration])
        t.start()

def onKeyPress(key):
    # Terminate
    if key == keyboard.Key.esc:
        keyboard_listener.stop()
        keyboard_listener.join()
        return
    if key == keyboard.Key.delete:
        # time.sleep(1.4)
        start()
        return
    
keyboard_listener = keyboard.Listener(
    on_press=onKeyPress
)
keyboard_listener.start()
keyboard_listener.join()
