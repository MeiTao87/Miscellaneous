
import cv2
import datetime
import requests
import numpy as np

#url = 'http://192.168.1.85:8080/shot.jpg'
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(1)

while True:
    # img_req = requests.get(url)
    # img_array = np.array(bytearray(img_req.content),dtype=np.uint8)
    # img = cv2.imdecode(img_array, -1)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #out.write(img)
    ret, img = cap.read()
    print(img.shape)
    #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Mobile video', img[:,:,2])
    #cv2.imshow('Mobile video gray', gray)
    #cv2.imshow('computer camear', gray_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#out.release()
#cap.release()
cv2.destroyAllWindows()