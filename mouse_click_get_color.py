#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:14:03 2020

@author: meitao
"""

import cv2
import numpy as np

# =============================================================================
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# =============================================================================

def click_and_crop(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, '  ', y)
        square_len = param
        blue = img[y-square_len:y+square_len, x-square_len:x+square_len, 0]
        green = img[y-square_len:y+square_len, x-square_len:x+square_len, 1]
        red = img[y-square_len:y+square_len, x-square_len:x+square_len, 2]
        print('blue.shape',blue.shape)
        print(blue)
        #cv2.circle(img, (y, x), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((square_len*2,square_len*2,3), np.uint8)
        print('mycolorImage.shape',mycolorImage[:,:,0].shape)
        mycolorImage[:, :, 0] = blue
        mycolorImage[:, :, 1] = green
        mycolorImage[:, :, 2] = red
        print(mycolorImage[:, :, 0])
        cv2.imshow('color',mycolorImage)

def nothing():
    pass

cap = cv2.VideoCapture(1)
cv2.namedWindow('para')
cv2.createTrackbar('square_len', 'para', 0, 200, nothing)

while True:
    _, img = cap.read()

    cv2.imshow('image', img)
    param = cv2.getTrackbarPos('square_len', 'para')
    cv2.setMouseCallback('image', click_and_crop, param)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()   
cv2.destroyAllWindows()
        
