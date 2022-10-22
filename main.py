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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

# test loop for dispensing based on number
numInitial = EmailRead.readEmails()

numNow = numInitial

while numNow <= numInitial:
    numNow = EmailRead.readEmails()
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
    print(numNow)


print("\n\nNew Email Alert!!!\n\n")
for i in range(10):
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.1)

GPIO.cleanup()
dispense.openDispenser(servoPin, servoFreq, servoStart, travelTime)
dispense.closeDispenser(servoPin, servoFreq, servoStart, travelTime)
p = Capture()
l = Capture.display(p, dispTime)

# # # end of script cleanup
GPIO.cleanup()


