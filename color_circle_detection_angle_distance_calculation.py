import cv2
import numpy as np
import requests
import math

# url = 'http://172.21.1.201:8080//shot.jpg'
cap = cv2.VideoCapture('/home/mt/Desktop/Smart System/4.mp4')

def nothing():
    pass

# Object 1
cv2.namedWindow('Tracking window for object 1')
cv2.createTrackbar('LH', 'Tracking window for object 1', 19, 255, nothing)
cv2.createTrackbar('UH', 'Tracking window for object 1', 32, 255, nothing)
cv2.createTrackbar('LS', 'Tracking window for object 1', 65, 255, nothing)
cv2.createTrackbar('US', 'Tracking window for object 1', 209, 255, nothing)
cv2.createTrackbar('LV', 'Tracking window for object 1', 100, 255, nothing)
cv2.createTrackbar('UV', 'Tracking window for object 1', 221, 255, nothing)
cv2.createTrackbar('dp', 'Tracking window for object 1', 2, 255, nothing)
cv2.createTrackbar('minDist', 'Tracking window for object 1', 37, 255, nothing)
switch = 'O:Off\n1:On'
cv2.createTrackbar(switch, 'Tracking window for object 1', 1, 1, nothing)
cv2.createTrackbar('angle_compensation', 'Tracking window for object 1', 0, 180, nothing)
angle_compensation_negative = '0:Posive\n1:Negative'
cv2.createTrackbar(angle_compensation_negative, 'Tracking window for object 1', 0, 1, nothing)

# Object 2
cv2.namedWindow('Tracking window for object 2')
cv2.createTrackbar('LH', 'Tracking window for object 2', 116, 255, nothing)
cv2.createTrackbar('UH', 'Tracking window for object 2', 210, 255, nothing)
cv2.createTrackbar('LS', 'Tracking window for object 2', 140, 255, nothing)
cv2.createTrackbar('US', 'Tracking window for object 2', 250, 255, nothing)
cv2.createTrackbar('LV', 'Tracking window for object 2', 119, 255, nothing)
cv2.createTrackbar('UV', 'Tracking window for object 2', 250, 255, nothing)
cv2.createTrackbar('dp', 'Tracking window for object 2', 2, 255, nothing)
cv2.createTrackbar('minDist', 'Tracking window for object 2', 37, 255, nothing)

# Object 3 for the two dots 
cv2.namedWindow('Tracking window for object 3')
cv2.createTrackbar('LH', 'Tracking window for object 3', 12, 255, nothing)
cv2.createTrackbar('UH', 'Tracking window for object 3', 20, 255, nothing)
cv2.createTrackbar('LS', 'Tracking window for object 3', 101, 255, nothing)
cv2.createTrackbar('US', 'Tracking window for object 3', 160, 255, nothing)
cv2.createTrackbar('LV', 'Tracking window for object 3', 184, 255, nothing)
cv2.createTrackbar('UV', 'Tracking window for object 3', 255, 255, nothing)
cv2.createTrackbar('dp', 'Tracking window for object 3', 2, 255, nothing)
cv2.createTrackbar('minDist', 'Tracking window for object 3', 37, 255, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    _, img = cap.read()
    img = cv2.resize(img, (800,600))
    # img_req = requests.get(url)
    # img_array = np.array(bytearray(img_req.content),dtype=np.uint8)
    # img = cv2.imdecode(img_array, -1)
    img_long, img_width, _ = img.shape
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # get value from TrackBars
    lh1 = cv2.getTrackbarPos('LH','Tracking window for object 1')
    uh1 = cv2.getTrackbarPos('UH','Tracking window for object 1')
    ls1 = cv2.getTrackbarPos('LS','Tracking window for object 1')
    us1 = cv2.getTrackbarPos('US','Tracking window for object 1')
    lv1 = cv2.getTrackbarPos('LV','Tracking window for object 1')
    uv1 = cv2.getTrackbarPos('UV','Tracking window for object 1')
    dp1 = cv2.getTrackbarPos('dp','Tracking window for object 1')
    minDist1 = cv2.getTrackbarPos('minDist','Tracking window for object 1')
    switch_value = cv2.getTrackbarPos(switch, 'Tracking window for object 1')
    angle_compensation = cv2.getTrackbarPos('angle_compensation', 'Tracking window for object 1')
    angle_compensation_sign = cv2.getTrackbarPos(angle_compensation_negative, 'Tracking window for object 1')

    lh2 = cv2.getTrackbarPos('LH','Tracking window for object 2')
    uh2 = cv2.getTrackbarPos('UH','Tracking window for object 2')
    ls2 = cv2.getTrackbarPos('LS','Tracking window for object 2')
    us2 = cv2.getTrackbarPos('US','Tracking window for object 2')
    lv2 = cv2.getTrackbarPos('LV','Tracking window for object 2')
    uv2 = cv2.getTrackbarPos('UV','Tracking window for object 2')
    dp2 = cv2.getTrackbarPos('dp','Tracking window for object 2')
    minDist2 = cv2.getTrackbarPos('minDist','Tracking window for object 2')
    
    lh3 = cv2.getTrackbarPos('LH','Tracking window for object 3')
    uh3 = cv2.getTrackbarPos('UH','Tracking window for object 3')
    ls3 = cv2.getTrackbarPos('LS','Tracking window for object 3')
    us3 = cv2.getTrackbarPos('US','Tracking window for object 3')
    lv3 = cv2.getTrackbarPos('LV','Tracking window for object 3')
    uv3 = cv2.getTrackbarPos('UV','Tracking window for object 3')
    dp3 = cv2.getTrackbarPos('dp','Tracking window for object 3')
    minDist3 = cv2.getTrackbarPos('minDist','Tracking window for object 3')

    lb1 = (lh1, ls1, lv1)
    ub1 = (uh1, us1, uv1)
    mask1 = cv2.inRange(hsv, lb1, ub1)
    lb2 = (lh2, ls2, lv2)
    ub2 = (uh2, us2, uv2)
    mask2 = cv2.inRange(hsv, lb2, ub2) 
    lb3 = (lh3, ls3, lv3)
    ub3 = (uh3, us3, uv3)
    mask3 = cv2.inRange(hsv, lb3, ub3)   
    
    # Morphological Operation
    kernel_erosion = np.ones((2, 2),np.uint8)
    # Erode: make white smaller or dispare
    erosion1 = cv2.erode(mask1, kernel_erosion, iterations=4) # eliminate noise (white dots)
    erosion2 = cv2.erode(mask2, kernel_erosion, iterations=3)
    erosion3 = cv2.erode(mask3, kernel_erosion, iterations=4)
    # Dilate: make white larger
    kernel_dilation = np.ones((4, 4), np.uint8)
    dilation1 = cv2.dilate(erosion1, kernel_dilation, iterations=4) # eliminate white dots inside the object
    dilation2 = cv2.dilate(erosion2, kernel_dilation, iterations=5)
    dilation3 = cv2.dilate(erosion3, kernel_dilation, iterations=4)
    # detecting circles
    ################################
    ### obj1 is at the moving axis
    ### obj2 is the rotating end
    ### obj3 is the two end points of the moving axis
    if switch_value == 1: # start to detect circles
        circles1 = cv2.HoughCircles(dilation1, cv2.HOUGH_GRADIENT, dp1, minDist1, param1=100, param2=30, minRadius=0, maxRadius=0)
        circles2 = cv2.HoughCircles(dilation2, cv2.HOUGH_GRADIENT, dp2, minDist2, param1=100, param2=30, minRadius=0, maxRadius=0)
        circles3 = cv2.HoughCircles(dilation3, cv2.HOUGH_GRADIENT, dp3, minDist3, param1=100, param2=30, minRadius=0, maxRadius=0)
        
        if circles1 is not None and circles2 is not None: # found first and second circle
            #print('Found first circle in image!!')
            #print('Found second circle in image!!')
            circle1 = np.around(circles1[0, :]).astype(int)
            circle2 = np.around(circles2[0, :]).astype(int)
            for (x1, y1, r1) in circle1:
                cv2.circle(img, (x1, y1), r1, (0, 0, 255), 4)  # red circle for the pedunlun
                cv2.rectangle(img, (x1-5, y1-5), (x1+5, y1+5), (0, 128, 255), -1)
                #cv2.line(img, (0, y1), (img_width, y1), (0, 0, 255), 1)
            for (x2, y2, r2) in circle2:
                cv2.circle(img, (x2, y2), r2, (0, 0, 255), 4)  # red circle for the pedunlun
                cv2.rectangle(img, (x2-5, y2-5), (x2+5, y2+5), (0, 128, 255), -1)

            # angle calculation:
            x_1 = x2 - x1
            y_1 = y2 - y1
            x_2 = 1
            y_2 = 0
            dot = x_1*x_2 + y_1*y_2      # dot product
            det = x_1*y_2 - y_1*x_2      # determinant
            angle = math.atan2(det, dot)/(math.pi)*180  # atan2(y, x) or atan2(sin, cos)
            if angle<0:
                if angle_compensation_sign == 1:
                    angle = 360 + angle - angle_compensation
                else:
                    angle = 360 + angle + angle_compensation
            else:
                if angle_compensation_sign == 1:
                    angle = angle - angle_compensation
                else:
                    angle = angle + angle_compensation
                
            cv2.putText(img, 'Angle is:'+str(angle), (10, 30), font, fontScale=0.6, color=(0,0,255))    
            
            
            # ###  moved this part upper, together with circles1
            # if circles2 is not None: # found second circle
            #     print('Found second circle in image!!')
            #     circle2 = np.around(circles2[0, :]).astype(int)
            #     for (x2, y2, r2) in circle2:
            #         cv2.circle(img, (x2, y2), r2, (0, 0, 255), 4)
            #         cv2.rectangle(img, (x2-5, y2-5), (x2+5, y2+5), (0, 128, 255), -1)
            #         #cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

        if circles3 is not None:  
            if (circles3[0,:,0].shape)[0] == 2: # only detect when there are two dots (same color)
                #print('Found more than one "third" circle in image!')
                circle3 = np.around(circles3[0, :]).astype(int)
                for (x3, y3, r3) in circle3:
                    cv2.circle(img, (x3, y3), r3, (0, 255, 0), 4)
                    cv2.rectangle(img, (x3-5, y3-5), (x3+5, y3+5), (255, 128, 0), -1)
                # drar a line between the two dots
                cv2.line(img, (circle3[0, 0], circle3[0, 1]), (circle3[1,0], circle3[1,1]), (0, 255, 0), 1)
                # distance calculation: ecudience distance
                # problem here: two circle3, didn't dicide which one first and which one is the second one
                if circles3[0][0][0]>circles3[0][1][0]:
                    # _1 is the right dot
                    x_3_1, y_3_1, x_3_2, y_3_2 = circles3[0][0][0], circles3[0][0][1], circles3[0][1][0],circles3[0][1][1]
                    dis_Left = np.sqrt((x1 - x_3_2)**2 + (y1 - y_3_2)**2)
                    dis_Right = np.sqrt((x1 - x_3_1)**2 + (y1 - y_3_1)**2)
                    cv2.putText(img, 'dis to Left is:'+str(dis_Left), (x_3_2, int(y_3_2-50)), font, fontScale=0.6, color=(0,0,255))
                    cv2.putText(img, 'dis to Right is:'+str(dis_Right), (x_3_1, int(y_3_1-50)), font, fontScale=0.6, color=(0,0,255))
                    # print('distance to Left',dis_Left)
                else:
                    # _1 is the left dot
                    x_3_1, y_3_1, x_3_2, y_3_2 = circles3[0][0][0], circles3[0][0][1], circles3[0][1][0],circles3[0][1][1]
                    dis_Left = np.sqrt((x1 - x_3_1)**2 + (y1 - y_3_1)**2)
                    dis_Right = np.sqrt((x1 - x_3_2)**2 + (y1 - y_3_2)**2)
                    cv2.putText(img, 'dis to Left is:'+str(dis_Left), (x_3_1, int(y_3_1-50)), font, fontScale=0.6, color=(0,0,255))
                    cv2.putText(img, 'dis to Right is:'+str(dis_Right), (x_3_2, int(y_3_2-50)), font, fontScale=0.6, color=(0,0,255))
                    # print('distance to Left',dis_Left)
                    
                

            
    
    # Show image
    cv2.imshow('img', img)
    cv2.imshow('Tracking window for object 1', dilation1)
    cv2.imshow('Tracking window for object 2', dilation2)
    cv2.imshow('Tracking window for object 3', dilation3)


    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()