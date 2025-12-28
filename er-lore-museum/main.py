import os
import cv2
import math
import pyautogui
import numpy as np
from mss import mss
from threading import Thread

from ui import setupUI, setPromptText

checkIdx = 0
locations = []
isWatchScreenPaused = False
isWatchScreenStopped = False
boundingBox = { 'top': 0, 'left': 0, 'width': 2560, 'height': 1440 }

# Load up images
def loadImages():
    fileNames = next(os.walk("./images"), (None, None, []))[2]
    
    for name in fileNames:
        img = cv2.imread(f'./images/{name}')
        sanitizedName = name.split("-")[0].capitalize()
        type = "title" if "title" in name else "vision"

        locations.append({
            "image": img,
            "type": type,
            "name": sanitizedName,
            "ignore": False
        })

def onWindowClose():
    global isWatchScreenStopped
    
    isWatchScreenStopped = True

def setWatchScreenPauseState(state: bool):
    global isWatchScreenPaused

    isWatchScreenPaused = state

def incrCheckIdx():
    global checkIdx

    if (checkIdx + 1 == len(locations)): # Start over if end reached
        checkIdx = 0
    else:
        checkIdx+= 1 # Check next img

def watchScreen():
    global checkIdx, boundingBox, isWatchScreenStopped, isWatchScreenPaused

    with mss() as sct:
        while True:
            if isWatchScreenStopped == True:
                break

            baseImage = locations[checkIdx]

            # Skip check if "paused" or if this image is being ignored
            if isWatchScreenPaused == True:
                continue
            if baseImage["ignore"] == True:
                incrCheckIdx()
                continue

            # Zone "title" check
            if baseImage["type"] == "title":
                try:
                    pyautogui.locateOnScreen(baseImage["image"], confidence=.6)
                    setPromptText(baseImage["name"])
                    setWatchScreenPauseState(True)
                    # Could change this to some `last_time_played` logic or smth
                    baseImage["ignore"] = True
                except pyautogui.ImageNotFoundException or RuntimeError:
                    incrCheckIdx()
            else: # "vision" check
                sct_img = sct.grab(boundingBox)
                imgArr = np.array(sct_img)

                # Source: https://medium.com/scrapehero/exploring-image-similarity-approaches-in-python-b8ca0a3ed5a3
                hist_img1 = cv2.calcHist([baseImage["image"]], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
                hist_img1[255, 255, 255] = 0 #ignore all white pixels
                cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

                hist_img2 = cv2.calcHist([imgArr], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
                hist_img2[255, 255, 255] = 0  #ignore all white pixels
                cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

                # Find the metric value
                metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
                roundedVal = round(metric_val, 2)                

                if roundedVal < 0.35 or math.isnan(roundedVal):
                    incrCheckIdx()
                else:
                    setPromptText(baseImage["name"])
                    setWatchScreenPauseState(True)
                    # Could change this to some `last_time_played` logic or smth
                    baseImage["ignore"] = True
                    # print(f"Found image {baseImage["name"]} with score:", roundedVal)


if __name__ == "__main__":
    loadImages()

    thread = Thread(target=watchScreen)
    thread.start()

    setupUI(onWindowClose, setWatchScreenPauseState)
