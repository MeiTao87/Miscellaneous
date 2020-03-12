#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:08:11 2020

@author: meitao
"""

import cv2 as cv

def nothing(x):
    print(x)
    
img = cv.imread('RGB.jpg')
cv.namedWindow('image')

switch = 'Color\nGrey'
cv.createTrackbar(switch, 'image', 0, 1, nothing)
cv.createTrackbar('CP', 'image', 0, 255, nothing)

while(1):
    img = cv.imread('RGB.jpg')
    
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (180, 180),font, 2, (0,0,255))
    
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.imshow('image',img)
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
