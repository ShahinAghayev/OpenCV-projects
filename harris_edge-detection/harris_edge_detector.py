import cv2
import numpy as np
cam = cv2.VideoCapture(0)

while 1:
    
    ret, frame = cam.read()
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #in the snippet above we capture frame and grayscale it#


    grayscaled = cv2.GaussianBlur(grayscaled, (3, 3), 0)
    harris = cv2.cornerHarris(grayscaled, 2, 3, 0.04)
    #here gaussian blur and harris are applied#
    #values in the harris part can be changed#

    
    threshold = 0.01 * harris.max()
    corners = np.zeros_like(grayscaled)
    corners[harris > threshold] = 255
    #this part is for finding possible corners#

    
    corners = cv2.dilate(corners, None)
    #this is optional but makes the corners more visible#

    
    cv2.imshow('Original',frame)
    cv2.imshow('Corners', corners)
    #here we display first the original footage then corners#
   
    if cv2.waitKey(5) == 27:
        break
        #here ESC is stop key#

cam.release()
cv2.destroyAllWindows()
