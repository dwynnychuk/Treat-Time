import RPi.GPIO as GPIO
import time
import dispense

servoPin = 32
servoFreq = 50
servoStart = 0
servoStop = 12

servoOutput = dispense.openDispenser(servoPin, servoFreq, servoStart)
dispense.closeDispenser(servoPin, servoFreq, servoStop, servoOutput)
GPIO.cleanup()


