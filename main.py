# # # IMPORTING
#import RPi.GPIO as GPIO
import dispense
import EmailRead
import EmailScrape
import time
from capture import Capture

# Next to do
# take starting from quickstart
# read email of sender
# send sender an email
# attach image to email
# bash script for continuous operation
# enclosure and cleanup


# # # SERVO INFORMATION
# Servo frequency is 50Hz
# 0DEGREE is DS of 2
# 180DEGREE is DS of 12

# # # INITIALIZATIONS
servoPin = 32
servoFreq = 50
servoStart = 2
servoStop = 12
ledPin = 18
travelTime = 1
dispTime = 5
blinkOnTime = 0.1
blinkOffTime = 0.05

# test loop for dispensing based on number
# numInitial = EmailRead.readEmails()
# numNow = numInitial

# while numNow <= numInitial:
#     numNow = EmailRead.readEmails()
#     print(numNow)


# print("\n\nNew Email Alert!!!\n\n")
# for i in range(5):
#     dispense.blink(ledPin, blinkOnTime, blinkOffTime)

#dispense.Dispenser(servoPin, servoFreq, servoStart, servoStop, travelTime)
#treatIm = Capture()
#Capture.display(treatIm, dispTime)

# # # # end of script cleanup
# GPIO.cleanup()

senderEmail, senderSubject = EmailScrape.scrapeSender()
print(senderEmail)
print(senderSubject)
dra = EmailScrape.emailDraft(senderEmail, senderSubject,'/home/pi/Documents/Treat-Time/images/2022-10-26 13:58:59.017654.jpg')
print(dra)