
import cv2
import datetime
import requests
import numpy as np
# http://192.168.1.65:8080/shot.jpg
# 
url = 'http://192.168.1.65:8080/shot.jpg'

while True:
    img_req = requests.get(url)
    img_array = np.array(bytearray(img_req.content),dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    #img_process = 
    cv2.imshow('Mobile video', img)

    if cv2.waitKey(1) == 27:
        break
