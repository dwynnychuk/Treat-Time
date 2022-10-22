# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


def openDispenser(servoPin, servoFreq, servoStart, travelTime):
    ledPin = 18
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(servoPin, GPIO.OUT)

    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(servoStart)
    servoOutput.ChangeDutyCycle(servoStart)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(travelTime)
    servoOutput.stop()
    

def closeDispenser(servoPin, servoFreq, servoStop, travelTime):
    ledPin = 18

    GPIO.output(ledPin, GPIO.LOW)
    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(0)
    servoOutput.ChangeDutyCycle(servoStop)
    time.sleep(travelTime)
    servoOutput.stop()
    