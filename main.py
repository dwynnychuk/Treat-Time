# # # IMPORTING
import RPi.GPIO as GPIO
import dispense
import EmailRead
import time
from capture import Capture

# # # SERVO INFORMATION
# Servo frequency is 50Hz
# 0DEGREE is DS of 2
# 180DEGREE is DS of 12

# # # INITIALIZATIONS
servoPin = 32
servoFreq = 50
servoStart = 2
servoStop = 12
ledPin = 18
travelTime = 1
dispTime = 5
blinkOnTime = 0.1
blinkOffTime = 0.05

# test loop for dispensing based on number
numInitial = EmailRead.readEmails()
numNow = numInitial

while numNow <= numInitial:
    numNow = EmailRead.readEmails()
    print(numNow)


print("\n\nNew Email Alert!!!\n\n")
for i in range(10):
    dispense.blink(ledPin, blinkOnTime, blinkOffTime)

dispense.Dispenser(servoPin, servoFreq, servoStart, servoStop, travelTime)
treatIm = Capture()
Capture.display(treatIm, dispTime)

# # # end of script cleanup
GPIO.cleanup()


