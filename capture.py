#access webcam and snap a photo 
import cv2
from datetime import datetime
import time
import os

# initiate directory for saving files
currentDirectory = os.getcwd()
saveDir = currentDirectory + "/images/"
print(saveDir)

# initiate camera
cam = cv2.VideoCapture(0)

# capture and save image
ret, image = cam.read()
timeNow = str(datetime.now().resolution(microseconds=1))
imDir = saveDir + timeNow + ".jpg"

time.sleep(1)
cv2.imwrite(imDir, image)

cv2.imread(imDir)
img = cv2.imread(imDir)
cv2.imshow("image",img)
cv2.waitKey(4000)

cam.release()
cv2.destroyAllWindows()