#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:04:40 2018

@author: anish
"""

import cv2

def main():
    windowName='Anish'
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    print("Width : "+str(cap.get(3)))  # width of resolution
    print("Height : "+str(cap.get(4)))  #height of resolution
    
    cap.set(3,1024)
    cap.set(4,1024)
    
    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret = False
    
    while ret:
        ret,frame = cap.read()
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break;
    cv2.destroyWindow(windowName)
    
    
    cap.release()
    
if __name__=="__main__":
    main()
    