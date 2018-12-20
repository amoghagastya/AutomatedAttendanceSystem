#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:08:13 2018

@author: anish
"""

import cv2

def main():
    imgpath = "AWs.png"
    img = cv2.imread(imgpath,0)
    cv2.imshow('Anish',img)
    cv2.imwrite('/Users/anish/Desktop/outputOpenCV/anish.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
    
    
if(__name__=="__main__"):
    main()