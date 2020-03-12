#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:11:45 2020

@author: meitao
"""

import cv2
import numpy as np

# =============================================================================
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# =============================================================================

### function to display mouse event, left click to display the position of click
### and right click to display the BGR channel values
global y
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, '  ', y)
         #cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 1:
            cv2.line(img, (0, points[-1][1]), (500,points[-1][1]), (255, 0, 0), 1)
        #cv2.line(img, (0, y), (500, y), (0, 255, 0), thickness=1)
        cv2.imshow('image',img)

        
#img = cv2.imread('RGB.jpg')
img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
points =[]

cv2.setMouseCallback('image', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows()
