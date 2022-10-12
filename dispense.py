# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


LED = 18
SERVO = 32
# set mode for pin numbering
# testing with LED
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SERVO, GPIO.OUT)

servoOutput = GPIO.PWM(SERVO,50)
servoOutput.start(0)

for i in range(13):
    GPIO.output(LED, GPIO.HIGH)
    servoOutput.ChangeDutyCycle(i)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)


servoOutput.stop()
# End of Script Cleanup
GPIO.cleanup()