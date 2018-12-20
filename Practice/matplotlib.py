#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:11:31 2018

@author: anish
"""

import cv2
import matplotlib.pyplot as plt 

def main():
    img = cv2.imread('AWs.png',1)
    #cv2.imshow('ANish',img)
    #img1 = cv2.imread('Documents.jpg',0)
   # cv2.imshow('ANish1',img1)
    #cv2.waitKey(0)
   # cv2.destroyAllWindows()
    plt.imshow(img,cmap='gray')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
if __name__=="__main__":
    main()