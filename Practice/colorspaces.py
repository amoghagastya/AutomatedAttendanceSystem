#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:32:25 2018

@author: anish
"""

import cv2
import matplotlib.pyplot as plt

def main():
    # cv2 reads image in the form of BGR but matplotlib reads image in the form RGB
    # So in order to display color images we need to change colorspace from RGB to BGR
    
    imgpath = "Aws.png"
    img = cv2.imread(imgpath)
    print(img)
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    print(img)
    
    plt.imshow(img)
    plt.show()
   
    
    
    
if __name__=="__main__":
    main()