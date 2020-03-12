import cv2
import numpy as np
from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)
# Read image 
img = cv2.imread('RGB.jpg', cv2.IMREAD_COLOR) # road.png is the filename
# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)
# Detect points that form a line
lines = probabilistic_hough_line(edges)
# Draw lines on the image
print('results: ',len(lines))
for line in lines:
    #print(line)
    x1, y1 = line[0]
    x2, y2 = line[1]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# Show result
cv2.imshow("Result Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()