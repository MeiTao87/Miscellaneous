#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:32:21 2020

@author: meitao
"""

import cv2
import numpy as np

img = cv2.imread('/home/mt/computer_vison/RGB.jpg')

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('/home/mt/Desktop/computer vision/1.jpg')


dim = (img.shape[1], img.shape[0])
#print(dim)
mask = np.zeros((img.shape), np.uint8)

mask = cv2.rectangle(mask,(0,0),(400,400),(200,200,200),-1)
cv2.imshow('maks',mask)
cv2.imshow('img',img)



print(type(mask))
print(type(img))
print(mask.dtype)
print(img.dtype)


#b,g,r = cv2.split(img)
#merge = cv2.merge((g,r,b)) #b, g, r

#scale_percent = 10 # percent of original size
#width = int(img2.shape[1] * scale_percent / 100)
#height = int(img2.shape[0] * scale_percent / 100)
#dim = (width, height)
# resize image
#img2 = cv2.resize(img2, dim)#, interpolation = cv2.INTER_AREA)
#img2 = cv2.resize(img2, dim)
#print(img2.shape)
#cv2.imshow('img',img)
#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)
#cv2.imshow('img2',img2)

#added_img = cv2.addWeighted(img, .5, img2, .5, 0)
#cv2.imshow('added_img',added_img)

bitAnd = cv2.bitwise_and(mask, img)
cv2.imshow('bitAnd',bitAnd)

bitOr = cv2.bitwise_or(mask, img)
cv2.imshow('bitOr',bitOr)

merge = cv2.add(bitAnd,bitOr)
cv2.imshow('merge',merge)

error = img-bitAnd
cv2.imshow('error',error)

cv2.waitKey(0)
cv2.destroyAllWindows()
