# # # IMPORTING
#import RPi.GPIO as GPIO
#import dispense
import EmailRead
#from capture import Capture


# # # INITIALIZATIONS
servoPin = 32
servoFreq = 50
servoStart = 0
servoStop = 12
travelTime = 1

num = EmailRead.readEmails()

#dispense.openDispenser(servoPin, servoFreq, servoStart, travelTime)
#dispense.closeDispenser(servoPin, servoFreq, servoStop, travelTime)

# # # capturing and saving image
#p = Capture()
#l = Capture().display(4)


# # # end of script cleanup
#GPIO.cleanup()


