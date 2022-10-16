#access webcam and snap a photo 
import cv2

# initiate camera
cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    cv2.imshow('Test',image)
    k = cv2.waitKey(1)
    if k != -1:
        break

cam.release()
cv2.destroyAllWindows()