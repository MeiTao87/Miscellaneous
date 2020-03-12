import cv2
import numpy as np

global h_min, h_max, s_min, s_max, v_min, v_max

h_min = 0
h_max = 0
s_min = 0
s_max = 0
v_min = 0
v_max = 0

def click_and_crop(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x, '  ', y)
        square_len = param
        img_ROI = img[y-square_len:y+square_len, x-square_len:x+square_len, :]
        hsv_ROI = cv2.cvtColor(img_ROI, cv2.COLOR_BGR2HSV)
        
        h_max = np.max(hsv_ROI[:, :, 0])
        h_min = np.min(hsv_ROI[:, :, 0])
        s_max = np.max(hsv_ROI[:, :, 1])
        s_min = np.min(hsv_ROI[:, :, 1])
        v_max = np.max(hsv_ROI[:, :, 1])
        v_min = np.min(hsv_ROI[:, :, 1])

        cv2.imshow('RIO',img_ROI)
        
        cv2.setTrackbarPos('h_min', 'para', h_min)
        cv2.setTrackbarPos('h_max', 'para', h_max)
        cv2.setTrackbarPos('s_min', 'para', s_min)
        cv2.setTrackbarPos('s_max', 'para', s_max)
        cv2.setTrackbarPos('v_min', 'para', v_min)
        cv2.setTrackbarPos('v_max', 'para', v_max)
        
        
        l_b = np.array([h_min, s_min, v_min])
        u_b = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(hsv_ROI, l_b, u_b)
       # res = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow('res', mask)
        cv2.imshow('image', img)




def nothing():
    pass

cap = cv2.VideoCapture(1)
cv2.namedWindow('para')
cv2.createTrackbar('square_len', 'para', 20, 200, nothing)
cv2.createTrackbar('h_min', 'para', h_min, 255, nothing)
cv2.createTrackbar('h_max', 'para', h_max, 255, nothing)
cv2.createTrackbar('s_min', 'para', s_min, 255, nothing)
cv2.createTrackbar('s_max', 'para', s_max, 255, nothing)
cv2.createTrackbar('v_min', 'para', v_min, 255, nothing)
cv2.createTrackbar('v_max', 'para', v_max, 255, nothing)

#def createTrackbar_1():



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
        
