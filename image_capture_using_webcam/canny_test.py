import cv2
import numpy as np
cap = cv2.VideoCapture(0)
 # 0 here is for webcam used by the computer#

#this is a continous loops it reads continuously till ESC key is pressed#
while(1):
    
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #here we are turning image from bgv to hsv#
    
    
    lower = np.array([0,0,0])
    upper = np.array([255,255,255])
    #these are hsv upper and lower values (by changing them various colors can be specified)#
    
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    
    cv2.imshow('Original',frame)
    # shows original camera footage)
    edges = cv2.Canny(frame,100,200)
    
    cv2.imshow('Edges',edges)
    #shows the generated edges image#
    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
#this is the part for detecting ESC key press#
    
    
cap.release()
cv2.destroyAllWindows()