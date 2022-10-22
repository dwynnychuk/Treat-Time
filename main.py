# # # IMPORTING
import RPi.GPIO as GPIO
import dispense
import EmailRead
import time
from capture import Capture


# # # INITIALIZATIONS
servoPin = 32
servoFreq = 50
servoStart = 0
servoStop = 12
ledPin = 18
travelTime = 1
dispTime = 5
blinkTime = 0.1

# test loop for dispensing based on number
numInitial = EmailRead.readEmails()

numNow = numInitial

#while numNow <= numInitial:
#    numNow = EmailRead.readEmails()
#    print(numNow)


print("\n\nNew Email Alert!!!\n\n")
#for i in range(10):
#    dispense.blink(ledPin, blinkTime)
#    time.sleep(blinkTime)

dispense.openDispenser(servoPin, servoFreq, servoStart, travelTime)
dispense.closeDispenser(servoPin, servoFreq, servoStart, travelTime)
p = Capture()
l = Capture.display(p, dispTime)

# # # end of script cleanup
GPIO.cleanup()


