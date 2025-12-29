from pynput import keyboard
from datetime import datetime

allowedKeys = ["w", "a", "s", "d", "]", "1", "2", "3", "4", "5"]
keyHistory = []
shouldListen = False

def isKeyAllowed(key: keyboard.Key | keyboard.KeyCode):
   global allowedKeys

   return key == keyboard.Key.space or (isinstance(key, keyboard.KeyCode) and key.char in allowedKeys)

def on_key_press(key: keyboard.Key | keyboard.KeyCode):
  global keyHistory, shouldListen

  print("Key", key)

  # Terminate
  if key == keyboard.Key.esc:
    print("Done listening.", keyHistory)

    keyboard_listener.stop()
    keyboard_listener.join()
    return

  if key == keyboard.Key.delete:
    print("Start listening...")
    shouldListen = True
    keyHistory.append({ "key": "delete", "startAt": datetime.now().strftime("%M:%S:%f") })
    return
  
  # Checking only specific keys
  if isKeyAllowed(key) == False or shouldListen == False:
    return

  if key == keyboard.Key.space:
    key = "space"

  # We do not spam same key multiple times. Key cannot be pressed 2 times in a row
  isThisKeyReleased = len(list(filter(lambda recordedKey: recordedKey["key"] == key and "endAt" not in recordedKey, keyHistory))) == 0
  
  if (isThisKeyReleased == False):
     return

  keyHistory.append({ "key": key, "startAt": datetime.now().strftime("%M:%S:%f") })

def on_key_release(key):
    global keyHistory, shouldListen

    if isKeyAllowed(key) == False or shouldListen == False:
        return
    
    if key == keyboard.Key.space:
      key = "space"

    indexes = [i for i, recordedKey in enumerate(keyHistory) if recordedKey["key"] == key and "endAt" not in recordedKey]
    thisKey = keyHistory[indexes[0]]

    if (thisKey == None):
       return

    keyHistory[indexes[0]]["endAt"] = datetime.now().strftime("%M:%S:%f")

keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)

print("Started")
keyboard_listener.start()
keyboard_listener.join()