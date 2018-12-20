#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:09:04 2018

@author: anish
"""

import cv2

def main():
    j=0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j=j+1
    print(j);
    
main()