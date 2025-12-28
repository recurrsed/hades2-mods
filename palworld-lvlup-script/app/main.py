import time
import vgamepad as vg

gamepad = vg.VX360Gamepad()

def triggerConfirm():
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(.02)
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()
    time.sleep(.02)

def openBuildMenu():
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    gamepad.update()
    time.sleep(.02)
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    gamepad.update()

def onStart():
    # open build menu
    openBuildMenu()
    time.sleep(.08)
    
    # navigate to build item
    gamepad.right_joystick(16768, 30000)
    gamepad.update()
    time.sleep(.05)

    # select item
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(.02)
    gamepad.right_joystick(0, 0)
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(.02)

    # build
    time.sleep(.02)
    triggerConfirm()

    # open build menu
    openBuildMenu()
    time.sleep(.02)

    # switch to destruct
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    gamepad.update()
    time.sleep(.02)
    gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    gamepad.right_joystick(0, 0)
    gamepad.update()
    time.sleep(.02)

    # confirm destruct
    triggerConfirm()

def main():
    time.sleep(2)
    while True:
        onStart()

if __name__ == "__main__":
    main()
