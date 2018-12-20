#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:58:27 2018

@author: anish
"""

import os
from PIL import Image
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

x_train = []
y_label = []
label_ids = {}
current_id = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(BASE_DIR,"anish")
recognizer = cv2.face.createLBPHFaceRecognizer()

for root,dirs,files in os.walk(image_path):
    for file in files :
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(root).lower()
            if not label in label_ids:
                label_ids[label] = current_id
                current_id+=1
            _id = label_ids[label]
            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image,"uint8")
            faces = face_cascade.detectMultiScale(image_array,1.3,5)
            for (x,y,w,h) in faces:
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_label.append(_id)

with open('labels.pickle','wb') as f:
    pickle.dump(label_ids,f) 


recognizer.train(x_train,np.array(y_label))
recognizer.save("trainner.yml")
              