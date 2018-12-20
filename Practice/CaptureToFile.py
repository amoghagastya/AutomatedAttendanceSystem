#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:27:39 2018

@author: anish
"""

import cv2

def main():
    windowName='Live Web Cam Capture'
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    filename = "/Users/anish/Desktop/outputOpenCV/output.mp4"
    codec = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate = 30
    resolution = (500,500)
    VideoFileOutput = cv2.VideoWriter(filename,codec,framerate,resolution)
    
    
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
        VideoFileOutput.write(frame)
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1)==27:
            break;
    cv2.destroyWindow(windowName)
    
    
    cap.release()
    
if __name__=="__main__":
    main()
    