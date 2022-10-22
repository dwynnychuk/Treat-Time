# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


def openDispenser(servoPin, servoFreq, servoStart, travelTime):    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)

    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(servoStart)
    print("open")
    servoOutput.ChangeDutyCycle(servoStart)
    time.sleep(travelTime)
    servoOutput.stop()
    

def closeDispenser(servoPin, servoFreq, servoStop, travelTime):
    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(0)
    print("close")
    servoOutput.ChangeDutyCycle(servoStop)
    time.sleep(travelTime)
    servoOutput.stop()


def blink(ledPin, blinkTime):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(blinkTime)
    GPIO.output(ledPin, GPIO.LOW)
    