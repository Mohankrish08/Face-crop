# Importing libraries

from ultralytics import YOLO
import cv2
import numpy as np
import cvzone
import argparse

# Arg parser
parser = argparse.ArgumentParser(description='Setup')
parser.add_argument('--image', default='Images', type=str, help='Path of the image')
parser.add_argument('--weight', default='Weights', type=str, help='weights for the model')
args =  parser.parse_args()

# Setup

image_path = args.image
weights_path = args.weight


# loading the model

model = YOLO(weights_path)


# loading image for inference

image = cv2.imread(image_path)
results = model(image)
for r in results:
    boxes = r.boxes
    labels = r.names
    name = list(labels.values())
    name_txt = str(name)
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2-x1, y2-y1
        cv2.rectangle(image, (x1,y1),(x2,y2), (0,0,255), 5)
        cvzone.putTextRect(image, name_txt,(max(0,x1), max(25,y1)))

cv2.imshow('img', image)
cv2.waitKey(0)


