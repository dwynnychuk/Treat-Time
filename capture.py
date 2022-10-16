#access webcam and snap a photo 
import cv2
from datetime import datetime
import time
import os

# initiate directory for saving files
currentDirectory = os.getcwd()
saveDir = currentDirectory + "/images"
print(saveDir)

# initiate camera
cam = cv2.VideoCapture(0)

# capture and save image
ret, image = cam.read()
timeNow = str(datetime.now())
cv2.imshow('Test',image)
cv2.waitKey(1000)
time.sleep(1)
cv2.imwrite(saveDir+timeNow, image)
print("check dir")
#    k = cv2.waitKey(1)
#    if k != -1:
#        break

cam.release()
cv2.destroyAllWindows()