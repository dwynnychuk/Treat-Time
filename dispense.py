# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


def openDispenser():
    ledPin = 18
    servoPin = 32
    servoFreq = 50
    servoStart = 0
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(servoPin, GPIO.OUT)

    servoOutput = GPIO.PWM(servoPin,servoFreq)
    servoOutput.start(servoStart)
    GPIO.output(ledPin, GPIO.HIGH)

def closeDispenser():
    # comment

# set mode for pin numbering
# testing with LED
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SERVO, GPIO.OUT)

servoOutput = GPIO.PWM(SERVO,50)
servoOutput.start(0)

for i in range(12):
    GPIO.output(LED, GPIO.HIGH)
    servoOutput.ChangeDutyCycle(i)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)


servoOutput.stop()
# End of Script Cleanup
GPIO.cleanup()