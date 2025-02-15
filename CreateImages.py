import cv2
import numpy as np

import os

# Directories to ensure they exist
directories = [
    "data/Forward", "data/Left", "data/Right",
    "data/Down", "data/Shoot", "data/Super",  "data/Nothing"
]

for dir in directories:
    if not os.path.exists(dir):
        os.makedirs(dir)  # This will create any missing directories


data = np.load("training_data.npy")
targets = np.load("target_data.npy")

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_up = 0
count_left = 0
count_right = 0
count_down = 0
count_shoot = 0
count_super = 0
count_go = 0
count_nothing = 0

for data in holder_list:
    #print(data[1])
    if data[1] == 'W':
        count_up += 1
        cv2.imwrite(f"data/Forward/H7-u{count_up}.png", data[0]) 
    elif data[1] == 'A':
        count_left += 1
        cv2.imwrite(f"data/Left/H7-l{count_left}.png", data[0]) 
    elif data[1] == 'D':
        count_right += 1
        cv2.imwrite(f"data/Right/H7-r{count_right}.png", data[0]) 
    elif data[1] == 'S':
        count_down += 1
        cv2.imwrite(f"data/Down/H7-d{count_down}.png", data[0]) 
    elif data[1] == ' ':
        count_shoot += 1
        cv2.imwrite(f"data/Shoot/H7-s{count_shoot}.png", data[0]) 
    elif data[1] == 'E':
        count_super += 1
        cv2.imwrite(f"data/Super/H7-e{count_super}.png", data[0]) 
    else:
        count_nothing += 1
        cv2.imwrite(f"data/Nothing/H7-n{count_nothing}.png", data[0]) 
