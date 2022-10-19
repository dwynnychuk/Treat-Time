class Capture:

    import cv2
    from datetime import datetime
    import time
    import os
    
    def __init__(self):
        import cv2
        from datetime import datetime
        import time
        import os
        timeNow = str(datetime.now())
        self.dir = os.getcwd() + "/images/" + timeNow + ".jpg"
        cam = cv2.VideoCapture(0)
        self.ret, self.image = cam.read()
        cv2.imwrite(self.dir, self.image)
        cam.release()

    def display(self,dispTime):
        import cv2
        from datetime import datetime
        import time
        import os
        self.img = cv2.imread(self.dir)
        cv2.imshow("Image",self.img)
        cv2.waitKey(dispTime*1000)
        cv2.destroyAllWindows()

#access webcam and snap a photo 


# # initiate directory for saving files
# currentDirectory = os.getcwd()
# saveDir = currentDirectory + "/images/"
# print(saveDir)

# # initiate camera
# cam = cv2.VideoCapture(0)

# # capture and save image
# ret, image = cam.read()
# timeNow = str(datetime.now())
# imDir = saveDir + timeNow + ".jpg"

# time.sleep(1)
# cv2.imwrite(imDir, image)

# cv2.imread(imDir)
# img = cv2.imread(imDir)
# cv2.imshow("image",img)
# cv2.waitKey(4000)

# cam.release()
# cv2.destroyAllWindows()