# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:29:37 2024

@author: Amine TEFFAL
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:23:19 2024

@author: Amine TEFFAL

from : https://www.youtube.com/watch?v=aFNDh5k3SjU
"""
import cv2
import numpy as np

from PIL import Image

# from utils import get_limits

yellow = [0, 255, 255] # this is yellow color in BGR space


def get_limits(color):

        c = np.uint8([[color]])
        hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
        
        lowerLimit = hsvC[0][0][0]-10, 100, 100
        upperLimit = hsvC[0][0][0]+10, 255, 255
        
        lowerLimit = np.array(lowerLimit, dtype=np.uint8)
        upperLimit = np.array(upperLimit, dtype=np.uint8)
        
        return lowerLimit, upperLimit

cap = cv2.VideoCapture(0)


while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    
    lowerLimit, upperLimit = get_limits(color=yellow)
    
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    
    mask_ = Image.fromarray(mask)
    
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame = cv2.rectangle(frame, (x1, y1), (x2,y2), (0,255,0), 5)
        
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()


cv2.destroyAllWindows()

print("OK")
