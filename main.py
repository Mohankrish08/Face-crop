# Importing Libraries

import cv2
from ultralytics import YOLO
import numpy as np
import os
from PIL import Image
import argparse


# arg parse
parser = argparse.ArgumentParser(description='setup')
parser.add_argument('--folder', default='Folder', type=str, help='path of the folder')
parser.add_argument('--weights', default='weights', type=str, help='weights for the model')
parser.add_argument('--output_folder', default='out folder', type=str, help='output folder')
args = parser.parse_args()

# setup
path = args.folder
weights_path = args.weights
output = args.output_folder

# model
model = YOLO(weights_path)

# Path
folder_path = path

# main 
new_folder = output
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
for dir in os.listdir(folder_path):
    alter_path = os.path.join(folder_path, dir)
    #print(alter_path)
    img_name, ext = os.path.splitext(dir)
    image = cv2.imread(os.path.join(folder_path,  dir))
    #print(image)
    results = model(image)
    for r in results:
        boxes, labels = r.boxes, r.names
        name = str(list(labels.values()))
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            #cv2.rectangle(image, (x1,y1),(x2,y2), (0,0,255), 20)
            face = image[y1:y2, x1:x2]
            crop = Image.fromarray(face[..., ::-1])
            crop_path = os.path.join(new_folder, f'{img_name}.jpg')
            crop.save(crop_path)

