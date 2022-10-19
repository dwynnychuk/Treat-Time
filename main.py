import RPi.GPIO as GPIO
import time
import dispense
#import EmailRead
from capture import Capture


servoPin = 32
servoFreq = 50
servoStart = 0
servoStop = 12
travelTime = 1

#num = EmailRead.readEmails()

dispense.openDispenser(servoPin, servoFreq, servoStart, travelTime)
dispense.closeDispenser(servoPin, servoFreq, servoStop, travelTime)

p = Capture()
l = Capture().display(4)

# end of script cleanup
GPIO.cleanup()


