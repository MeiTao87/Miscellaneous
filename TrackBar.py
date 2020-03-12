#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:53:13 2020

@author: meitao
"""

import cv2 as cv
import numpy as np

def nothing(x):
    print(x)
    
img = np.ones((300, 512, 3), np.uint8)*200
cv.imshow('aaa',img)
cv.namedWindow('image')

switch = '0:OFF 1:ON'

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = img[:]
    else:
        img[:] = [b, g, r]
        

cv.destroyAllWindows()
