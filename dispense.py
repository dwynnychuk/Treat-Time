# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


def Dispenser(servoPin, servoFreq, servoStart, servoStop, travelTime):    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)

    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(0)
    servoOutput.ChangeDutyCycle(servoStart)
    time.sleep(travelTime)
    servoOutput.ChangeDutyCycle(servoStop)
    time.sleep(travelTime)
    servoOutput.stop()


def blink(ledPin, blinkOnTime, blinkOffTime):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(blinkOnTime)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(blinkOffTime)
    