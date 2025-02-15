import numpy as np
import cv2
import time
import os
from grabscreen import grab_screen
from getkeys import key_check


file_name = "training_data.npy"
file_name2 = "target_data.npy"
dirct_name = "data"

def get_data(): 

    if os.path.isfile(file_name):
        print('File exists, loading previous data!')
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))
    else:
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        os.makedirs(os.path.dirname(file_name2), exist_ok=True)
        print('File does not exist, starting fresh!')
        image_data = []
        targets = []
    return image_data, targets


def save_data(image_data, targets):

    np.save(file_name, image_data) 
    np.save(file_name2, targets)


image_data, targets = get_data()
while True:
    keys = key_check()
    print("waiting press B to start")
    if keys == "B":
        print("Starting")
        break

count = 0
while True:
    count +=1
    last_time = time.time()
    image = grab_screen(region=(50, 100, 1500, 800))


    # Debug line to show image
    cv2.imshow("AI Peak", image)
    cv2.resize( image, (500, 800))
    cv2.waitKey(1)

    # Convert to numpy array
    image = np.array(image)
    image_data.append(image)

    keys = key_check()
    targets.append(keys)
    if keys == "H":
        break


    print('loop took {} seconds'.format(time.time()-last_time), "Key="+ keys)



save_data(image_data, targets)
if os.path.exists(file_name):
    print("File saved successfully:", file_name)
else:
    print("Failed to save file:", file_name)

if os.path.exists(file_name2):
    print("File saved successfully 2:", file_name2)
else:
    print("Failed to save file 2:", file_name2)