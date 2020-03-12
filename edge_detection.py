import cv2
import numpy as np
import requests
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line)
import matplotlib.pyplot as plt

#url = 'http://192.168.1.65:8080/shot.jpg'
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)

# make a parameter adjust window
def nothing():
    pass

cv2.namedWindow('GUS_ADJ')
cv2.createTrackbar('Gus_blur', 'GUS_ADJ', 4, 10, nothing)

while True:
    gus_pos = cv2.getTrackbarPos('Gus_blur','GUS_ADJ')
    gus_odd_pos = int(gus_pos*2)+1
    
    #img_req = requests.get(url)
    #img_array = np.array(bytearray(img_req.content),dtype=np.uint8)
    #img = cv2.imdecode(img_array, -1)
    _, img = cap.read()
    kernel = np.ones((5,5),np.float32)/25
    gimg = cv2.GaussianBlur(img, (gus_odd_pos,gus_odd_pos), 0)

    #image = np.mean(img, axis=2)
    #print(image.shape)
    #hspace, angles, distances = hough_line(image)
    #angle=[]
    #for _, a , distances in zip(*hough_line_peaks(hspace, angles, distances)):
    #    angle.append(a)

    # Obtain angle for each line
    #angles = [a*180/np.pi for a in angle]

    # Compute difference between the two lines
    #angle_difference = np.max(angles) - np.min(angles)
    #print(angle_difference)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #laplacian = cv2.Laplacian(img, cv2.CV_64F)
    #sobelx = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=5)
    #sobely = cv2.Sobel(img,cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(img, 100, 200)
    gedges = cv2.Canny(gimg, 100, 200)

    #### Hough transform
    lines = probabilistic_hough_line(gedges, threshold=10, line_length=5, line_gap=5)
    print(len(lines))
    print(' ')
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        #((p0[0], p1[0]), (p0[1], p1[1]))
        lineThickness = 2
        cv2.line(img, (x1, y1), (x2, y2), (0,255,0), lineThickness)

    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(gimg, str(gus_odd_pos), (180, 180),font, 2, (0,0,255))


    cv2.imshow('image',img)
    cv2.imshow('gimage',gimg)
    #cv2.imshow('image_trans',image)
    #cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelx',sobelx)
    #cv2.imshow('sobely',sobely)
    cv2.imshow('edges',edges)
    cv2.imshow('gedges',gedges)
    #cv2.imshow('plot_lines',plot_lines)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

#out.release()
#cap.release()
cv2.destroyAllWindows()
