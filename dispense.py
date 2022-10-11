# Dispense treat by moving servo

import RPi.GPIO as GPIO
import time


LED = 18
# set mode for pin numbering
# testing with LED
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)

for i in range(30):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.2)


# End of Script Cleanup
GPIO.cleanup()