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


print("New Email Alert")
for i in range(50):
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.2)




#dispense.openDispenser(servoPin, servoFreq, servoStart, travelTime)
#dispense.closeDispenser(servoPin, servoFreq, servoStop, travelTime)

# # # capturing and saving image
#p = Capture()
#l = Capture().display(4)


# # # end of script cleanup
GPIO.cleanup()


