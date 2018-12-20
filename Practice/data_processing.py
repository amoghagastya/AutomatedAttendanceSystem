#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:15:55 2018

@author: anish
"""

import cv2

def main():
    imgpath = "Aws.png"
    img = cv2.imread(imgpath)
  #  img = cv2.imread(imgpath,0) - for gray image
    cv2.namedWindow('Anish',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Anish',img)
    cv2.waitKey(0)
    cv2.destroyWindow('Anish')
    
if(__name__=="__main__"):
    main()