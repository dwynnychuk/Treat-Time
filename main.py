import RPi.GPIO as GPIO
import time
import dispense

servoPin = 32
servoFreq = 50
servoStart = 0
servoStop = 12

dispense.openDispenser(servoPin, servoFreq, servoStart)
dispense.closeDispenser(servoPin, servoFreq, servoStop)
GPIO.cleanup()


