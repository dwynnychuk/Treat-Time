import RPi.GPIO as GPIO
import time
import dispense

servoPin = 32
servoFreq = 50
servoStart = 0
servoStop = 12
travelTime = 1

dispense.openDispenser(servoPin, servoFreq, servoStart, travelTime)
dispense.closeDispenser(servoPin, servoFreq, servoStop, travelTime)


# end of script cleanup
GPIO.cleanup()

