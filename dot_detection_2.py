import cv2
import numpy as np
import requests
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line)
import matplotlib.pyplot as plt
import requests

def nothing():
    pass

cv2.namedWindow('ADJ_Window')
cv2.createTrackbar('Gus_blur', 'ADJ_Window', 4, 10, nothing)
cv2.createTrackbar('kernel number', 'ADJ_Window', 5, 10, nothing)

# Bar for HSV
cv2.createTrackbar('LH', 'ADJ_Window', 0, 255, nothing)
cv2.createTrackbar('UH', 'ADJ_Window', 255, 255, nothing)
cv2.createTrackbar('LS', 'ADJ_Window', 0, 255, nothing)
cv2.createTrackbar('US', 'ADJ_Window', 255, 255, nothing)
cv2.createTrackbar('LV', 'ADJ_Window', 0, 255, nothing)
cv2.createTrackbar('UV', 'ADJ_Window', 255, 255, nothing)

img = cv2.imread('green.jpg')
output = img.copy()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
l_h = cv2.getTrackbarPos('LH','ADJ_Window')
l_s = cv2.getTrackbarPos('LS','ADJ_Window')
l_v = cv2.getTrackbarPos('LV','ADJ_Window')
u_h = cv2.getTrackbarPos('UH','ADJ_Window')
u_s = cv2.getTrackbarPos('US','ADJ_Window')
u_v = cv2.getTrackbarPos('UV','ADJ_Window')
    
l_b = np.array([l_h, l_s, l_v])
u_b = np.array([u_h, u_s, u_v])
    
mask = cv2.inRange(hsv, l_b, u_b)
res = cv2.bitwise_and(img, img, mask=mask)

gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    

    # detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    # ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
cv2.imshow("output", np.hstack([res, output]))