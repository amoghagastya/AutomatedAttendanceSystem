#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 00:34:45 2018

@author: anish
"""

import cv2
import numpy as np

def main():
    img1 = np.zeros((512,512,3),np.uint8)
    
    cv2.line(img1,(0,10),(90,0),(255,0,0),0)
    cv2.rectangle(img1,(50,60),(30,80),(255,255,0),4)
    cv2.circle(img1,(60,60),10,(0,255,255),3)
    text = 'Anish th great'
    cv2.putText(img1,text,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))
    cv2.imshow('ANish',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    
    
if(__name__=="__main__"):
    main()