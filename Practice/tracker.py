#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 01:12:29 2018

@author: anish
"""

import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    img1 = np.zeros((512,512,3),np.uint8)
    windowName="Anish"
    cv2.namedWindow(windowName)
    cv2.createTrackbar('B',windowName,0,255,emptyFunction)
    cv2.createTrackbar('G',windowName,0,255,emptyFunction)
    cv2.createTrackbar('R',windowName,0,255,emptyFunction)
    while True:
        cv2.imshow(windowName,img1)
        blue = cv2.getTrackbarPos('B',windowName)
        green = cv2.getTrackbarPos('G',windowName)
        red = cv2.getTrackbarPos('R',windowName)
        img1[:] = [blue,green,red]
        if cv2.waitKey(1)==27:
            break;
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()