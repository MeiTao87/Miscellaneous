

import cv2
import datetime
#import numpy as np
cap = cv2.VideoCapture(-1);
print('width',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height',cap.get(4))


while(True):
    ret, frame = cap.read()
    
    #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_COMPLEX
    #text = 'Height: ' + str(cap.get(4)) + ' Width: ' + str(cap.get(3))
    date_time = str(datetime.datetime.now())
    frame = cv2.putText(frame, date_time, (10,50), font, 1, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
