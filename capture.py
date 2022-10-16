#access webcam and snap a photo 
import cv2
from datetime import datetime

# initiate camera
cam = cv2.VideoCapture(0)

# capture and save image
ret, image = cam.read()
cv2.imshow('Test',image)
cv2.waitKey(1000)
#    k = cv2.waitKey(1)
#    if k != -1:
#        break

cam.release()
cv2.destroyAllWindows()