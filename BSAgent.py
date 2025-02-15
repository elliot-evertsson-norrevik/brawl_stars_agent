import random
import time
from getkeys import key_check
import pydirectinput
import keyboard
import cv2
from grabscreen import grab_screen
from directkeys import PressKey, ReleaseKey, W, D, A, S
from fastai.vision.all import *
import pathlib

# Fix for PosixPath issue on Windows
pathlib.PosixPath = pathlib.WindowsPath

# Define label_func before loading the model if it was used in training
def label_func(x): return x.parent.name

# Load the model from the Windows path
model_path = "model/bs_model.pkl"
learn_inf = load_learner(model_path)
print("loaded learner")

# Sleep time after actionsbss
sleepy = 0.01

# Wait for me to push B to start.fhf
time.sleep(sleepy)

# Randomly pick action then sleep.
# 0 do nothing release everything ( except W )sssssssssssssssssssssssjhdd
# 1 hold left
# 2 hold rightw 
# 3 Press Jump


while True:
    image = grab_screen(region=(50, 100, 1500, 800))
    keyboard.press('a')
    cv2.imshow("AI Peak", image)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]

    if action == "Down" or result[2][0] > .1:
        print(f"DOWN! - {result[1]}")
        keyboard.press("S")
        keyboard.release("S")


    if action == "Forward":
        print(f"FORWARD! - {result[1]}")
        keyboard.press("W")
        keyboard.release("W")



    elif action == "Left":
        print(f"LEFT! - {result[1]}")
        keyboard.press("A")
        keyboard.release("A")

  

    elif action == "Right":
        print(f"Right! - {result[1]}")
        keyboard.press("D")
        keyboard.release("D")


    elif action == "Shoot":
        print(f"FIRE IN THE HOLE! - {result[1]}")
        keyboard.press("space")
        keyboard.release("space")


    # End simulation by hitting 
    keys = key_check()
    if "H" in keys:
        break
