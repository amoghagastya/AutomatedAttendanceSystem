#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:01:51 2018

@author: anish
"""

import cv2
import matplotlib.pyplot as mpl

def main():
    print('Anish');
# for external frame cpature use 0 
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame = cap.read()
        print(ret)
        print(frame)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        mpl.imshow(frame)
        mpl.show()
        
    else:
        ret = False;
    cap.release() # releases the camera
    
if __name__=="__main__":
    main()