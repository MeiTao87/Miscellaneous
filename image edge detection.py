import cv2
import numpy as np
import requests
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line)
import matplotlib.pyplot as plt


# make a parameter adjust window
def nothing():
    pass

cv2.namedWindow('ADJ_Window')
cv2.createTrackbar('Gus_blur', 'ADJ_Window', 4, 10, nothing)
cv2.createTrackbar('kernel number', 'ADJ_Window', 5, 10, nothing)

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    #img = cv2.imread('1.jpg')  # import image
    #img = cv2.resize(img, (640,440))  # resie the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR to Gray

    gus_pos = cv2.getTrackbarPos('Gus_blur','ADJ_Window')  # get the parameter of gussian blur
    gus_odd_pos = int(gus_pos*2)+1  
    kernel_n= cv2.getTrackbarPos('kernel number','ADJ_Window')
    kernel = np.ones((kernel_n,kernel_n),np.float32)/(kernel_n*kernel_n)
    
    #gus_img = cv2.GaussianBlur(img, (gus_odd_pos,gus_odd_pos), 0)
    gus_gray_img = cv2.GaussianBlur(gray, (gus_odd_pos,gus_odd_pos), 0)
    
    #blur_img = cv2.filter2D(img,-1,kernel)
    blur_gray_img = cv2.filter2D(gray,-1,kernel)

    edges = cv2.Canny(gray, 100, 200)
    #gus_edges = cv2.Canny(gus_img, 100, 200)
    gus_gray_edge = cv2.Canny(gus_gray_img, 100, 200)
    blur_edge = cv2.Canny(blur_img, 100, 200)
    blur_gray_edge = cv2.Canny(blur_gray_img, 100, 200)

    #### Hough transform
    lines = probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=5)
    gus_lines = probabilistic_hough_line(gus_edges, threshold=10, line_length=5, line_gap=5)
    gus_gray_lines = probabilistic_hough_line(gus_gray_edge, threshold=10, line_length=5, line_gap=5)
    blur_lines = probabilistic_hough_line(blur_edge, threshold=10, line_length=5, line_gap=5)
    blur_gray_lines = probabilistic_hough_line(blur_gray_edge, threshold=10, line_length=5, line_gap=5)

    print(len(lines))
    print(' ')
    for line in blur_gray_lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        #((p0[0], p1[0]), (p0[1], p1[1]))
        lineThickness = 2
        cv2.line(img, (x1, y1), (x2, y2), (0,255,0), lineThickness)

    

    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gus_img, str(gus_odd_pos), (180, 180),font, 2, (0,0,255))


    cv2.imshow('image',img)
    cv2.imshow('gimage',blur_gray_img)
    cv2.imshow('edges',edges)
    cv2.imshow('gedges',gus_edges)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
