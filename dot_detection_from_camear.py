import cv2
import numpy as np
import requests
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line)
import matplotlib.pyplot as plt
import math

url = 'http://192.168.1.85:8080/shot.jpg'


# make a parameter adjust window
def nothing():
    pass      

cv2.namedWindow('ADJ_Window')
cv2.namedWindow('ADJ_Window_2')
#cv2.createTrackbar('Gus_blur', 'ADJ_Window', 4, 10, nothing)
#cv2.createTrackbar('kernel number', 'ADJ_Window', 5, 10, nothing)

# Bar for HSV
cv2.createTrackbar('LH', 'ADJ_Window', 36, 255, nothing)
cv2.createTrackbar('UH', 'ADJ_Window', 64, 255, nothing)
cv2.createTrackbar('LS', 'ADJ_Window', 49, 255, nothing)
cv2.createTrackbar('US', 'ADJ_Window', 255, 255, nothing)
cv2.createTrackbar('LV', 'ADJ_Window', 53, 255, nothing)
cv2.createTrackbar('UV', 'ADJ_Window', 255, 255, nothing)
switch = 'O:Off\n1:On'
cv2.createTrackbar(switch, 'ADJ_Window', 0, 1, nothing)

cv2.createTrackbar('LH_2', 'ADJ_Window_2', 73, 255, nothing)
cv2.createTrackbar('UH_2', 'ADJ_Window_2', 132, 255, nothing)
cv2.createTrackbar('LS_2', 'ADJ_Window_2', 49, 255, nothing)
cv2.createTrackbar('US_2', 'ADJ_Window_2', 255, 255, nothing)
cv2.createTrackbar('LV_2', 'ADJ_Window_2', 53, 255, nothing)
cv2.createTrackbar('UV_2', 'ADJ_Window_2', 223, 255, nothing)

cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    #img_req = requests.get(url)
    #img_array = np.array(bytearray(img_req.content),dtype=np.uint8)
    #img = cv2.imdecode(img_array, -1)
    #img_long, img_width, _ = img.shape
    #img = cv2.imread('green.jpg')
    #img = cv2.resize(img, (600,800))
    output = img.copy()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos('LH','ADJ_Window')
    l_s = cv2.getTrackbarPos('LS','ADJ_Window')
    l_v = cv2.getTrackbarPos('LV','ADJ_Window')
    u_h = cv2.getTrackbarPos('UH','ADJ_Window')
    u_s = cv2.getTrackbarPos('US','ADJ_Window')
    u_v = cv2.getTrackbarPos('UV','ADJ_Window')
    switch_on_off = cv2.getTrackbarPos(switch,'ADJ_Window')
    
    l_h_2 = cv2.getTrackbarPos('LH_2','ADJ_Window_2')
    l_s_2 = cv2.getTrackbarPos('LS_2','ADJ_Window_2')
    l_v_2 = cv2.getTrackbarPos('LV_2','ADJ_Window_2')
    u_h_2 = cv2.getTrackbarPos('UH_2','ADJ_Window_2')
    u_s_2 = cv2.getTrackbarPos('US_2','ADJ_Window_2')
    u_v_2 = cv2.getTrackbarPos('UV_2','ADJ_Window_2')
    
    # boudrays
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    l_b_2 = np.array([l_h_2, l_s_2, l_v_2])
    u_b_2 = np.array([u_h_2, u_s_2, u_v_2])
    
    mask_1 = cv2.inRange(hsv, l_b, u_b)
    mask_2 = cv2.inRange(hsv, l_b_2, u_b_2)
    res = cv2.bitwise_and(img, img, mask=mask_1) #using mask to filter color
    res_2 = cv2.bitwise_and(img, img, mask=mask_2)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    gray_2 = cv2.cvtColor(res_2, cv2.COLOR_BGR2GRAY)
    ###########  transform: erode and dilate
    ########  mask threshold and kernel size  #########
    _, mask_transform = cv2.threshold(gray,50, 200, cv2.THRESH_BINARY)
    _, mask_transform_2 = cv2.threshold(gray_2,50, 200, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    ######  iterrations  can be change later   ######
    dilation = cv2.dilate(mask_transform, kernel, iterations=5) # area of black dot get smaller
    dilation_2 = cv2.dilate(mask_transform_2, kernel, iterations=5) # area of black dot get smaller
    erosion = cv2.erode(dilation, kernel, iterations=5) # area of black get larger
    erosion_2 = cv2.erode(dilation_2, kernel, iterations=5) # area of black get larger

    if switch_on_off == 1:
        # detect circles in the image
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=0, maxRadius=0)
        circles_2 = cv2.HoughCircles(gray_2, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=0, maxRadius=0)
        x1, y1 = 1, 1
        x2, y2 = 1, 1
        # ensure at least some circles were found
        if circles is not None:
	        circles = np.around(circles[0, :]).astype(int)
        if circles_2 is not None:
	        circles_2 = np.round(circles_2[0, :]).astype(int)

        # draw the circle to visulize them
        if circles is not None and circles_2 is not None:
            for (x1, y1, r) in circles:
                cv2.circle(output, (x1, y1), r, (0, 0, 255), 4)
                cv2.rectangle(output, (x1 - 5, y1 - 5), (x1 + 5, y1 + 5), (0, 128, 255), -1)
            for (x2, y2, r2) in circles_2:
                cv2.circle(output, (x2, y2), r2, (0, 0, 255), 4)
                cv2.rectangle(output, (x2 - 5, y2 - 5), (x2 + 5, y2 + 5), (0, 128, 255), -1)

        # first horizantal line
        if x2 is not None and y2 is not None:
            cv2.line(output, (0, y2), (img_width, y2), (0, 0, 255), 1)
        # second slope line
        if x1 is not None and y1 is not None:
            cv2.line(output, (x1, y1), (x2, y2), (0, 0, 255), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        #angle calculation
        if x2 is not None and y2 is not None:
            if x1 is not None and y1 is not None:
                print(x1, '   ', y1)
                print(x2, '   ', y2)
                print('    ')
                x_1 = x1 - x2
                y_1 = y1 - y2
                x_2 = 1
                y_2 = 0
                dot = x_1*x_2 + y_1*y_2      # dot product
                det = x_1*y_2 - y_1*x_2      # determinant
                angle = math.atan2(det, dot)/(math.pi)*180  # atan2(y, x) or atan2(sin, cos)
                if angle<0:
                    angle = 360 + angle
                    # arctan_value = (y1-y2)/(x1-x2)
                    # angle = (math.atan(arctan_value))/(math.pi)*180
                print('angle: ', angle)
                cv2.putText(output, 'Angle is:'+str(angle), (10, 30),font, fontScale=0.6, color=(0,0,255))
    
    else:
        pass
    
    # show the output image  
    cv2.imshow('output', output)
    cv2.imshow('res',res)
    cv2.imshow('res2',res_2)
    cv2.imshow('erosion', erosion)
    cv2.imshow('gray',gray)

    key = cv2.waitKey(1)
    if key == 27:
        break
#cap.release()   
cv2.destroyAllWindows()
