#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:58:14 2018

@author: anish
"""

import cv2

def main():
    # [125,134,13]  - BLUE GREEN RED
    imgpath = "AWs.png"
    img = cv2.imread(imgpath,0)
    # the way image is stored
    print(type(img))
    #data type of each pixel
    print(img.dtype)
    #the resolution of image 
    print(img.shape)
    print(img.ndim)
    print(img.size)
   # cv2.imshow('Anish',img)
   # cv2.waitKey(0)
   # cv2.destroyAllWindows()  
    
if(__name__=="__main__"):
    main()