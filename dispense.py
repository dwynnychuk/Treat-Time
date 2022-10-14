# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


# def openDispenser(servoPin, servoFreq, servoStart):
#     ledPin = 18
    
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(ledPin, GPIO.OUT)
#     GPIO.setup(servoPin, GPIO.OUT)

#     servoOutput = GPIO.PWM(servoPin,servoFreq)
#     servoOutput.start(servoStart)
#     servoOutput.ChangeDutyCycle(servoStart+2)
#     GPIO.output(ledPin, GPIO.HIGH)
#     time.sleep(1)
#     #servoOutput.ChangeDutyCycle(servoStart+10)
#     GPIO.output(ledPin, GPIO.LOW)
    
#     return servoOutput

# def closeDispenser(servoPin, servoFreq, servoStop, servoOutput):

#     # GPIO.setmode(GPIO.BOARD)
#     # GPIO.setup(servoPin, GPIO.OUT)

#     # servoOutput = GPIO.PWM(servoPin,servoFreq)
#     # servoOutput.start(0)
#     servoOutput.ChangeDutyCycle(servoStop-1)
#     time.sleep(1)
#     servoOutput.stop()




def openDispenser(servoPin, servoFreq, servoStart):
    ledPin = 18
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(servoPin, GPIO.OUT)

    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(servoStart)
    servoOutput.ChangeDutyCycle(servoStart+2)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    #servoOutput.ChangeDutyCycle(servoStart+10)
    GPIO.output(ledPin, GPIO.LOW)
    servoOutput.stop()
    

def closeDispenser(servoPin, servoFreq, servoStop):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)

    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(0)
    servoOutput.ChangeDutyCycle(servoStop-1)
    time.sleep(1)
    servoOutput.stop()
    