import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('color_ball.jpg',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((10,10),np.uint8)

dilation = cv2.dilate(mask, kernel, iterations=10) # area of black dot get smaller
erosion = cv2.erode(mask, kernel, iterations=10) # area of black get larger
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # first erosion and then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #opposite of opening
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) # difference between erosion and dilation
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) # difference between original and opening

title = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(3, int(len(images)/3)+1, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()