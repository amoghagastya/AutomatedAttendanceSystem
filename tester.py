#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 07:30:15 2018

@author: anish
"""

import cv2
import os
import time
import numpy as np
import faceRecognition as fr
import sqlite3
import xlwt 
from xlwt import Workbook 


test_img = cv2.imread('/Users/anish/desktop/openCV/anish.JPG')
faces_detected,gray_img = fr.face_detection(test_img)
#for (x,y,w,h) in faces_detected:
 #   cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

conn = sqlite3.connect("Face-DataBase") 
cur = conn.cursor()
ex = "SELECT ID,Name from Students"
cur.execute(ex)
list1 = cur.fetchall()
faces,faceID = fr.labels_for_training_data('/Users/anish/desktop/openCV/dataset')
face_recognizer = fr.train_clasifier(faces,faceID)
name ={}
for i in list1:
    name[i[0]] = i[1]
print(name)
for face in faces_detected:
    (x,y,w,h) = face
    roi_gray = gray_img[y:y+w,x:x+h]
    label,confidence = face_recognizer.predict(roi_gray)
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name = name[label]
    print(predicted_name)
    fr.put_text(test_img,predicted_name,x,y)
#get current date
currentDate = time.strftime("%d_%m_%y")

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 

sheet1 = wb.add_sheet('Sheet 1') 


sheet1.write(0, 0, 'ROLL NO') 
sheet1.write(0, 1, 'NAME') 

sheet1.write(1,0,label)
sheet1.write(1,1,predicted_name)
  
wb.save('xlwt example.xls') 
resized_img = cv2.resize(test_img,(1000,700))
cv2.imshow("face detection",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()