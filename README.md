# Treat-Time
An automated email-based treat dispenser for my dog. 

# Inspiration
Working a demanding day job with a new puppy (Murphy) I often felt bad about leaving her alone while I was working. Wanting a way to interact with her throughout the work day this idea naturally came about.

# How it works
Upon running the code (main.py), the dog's email address is continually monitored for new emails. Upon recieving a new email, pertinant information is collected from the sender such as email address and subject line. A treat is dispensed using a servo and a dispense mechanism before a photo is captured using the onboard webcam. Concurrently, using the Google Gmail API, an email is drafted in reply to the sender with an automated message from Murphy thanking the sender for the treat. The captured image is attached to the email before it is sent off in a reply thread to the sender.

# Hardware
Raspberry Pi 3B+<br />
Logitech C270 webcam<br />
Tower Pro Arduino Servo (Hitec HS-65HB fits as an upgraded servo)<br />
On/Off switch for USB power <br />
Custom 3d Printed enclosure

# Pinout
Servo commmand (32)<br />
LED command (18) - optional

# Image
![ISO-Treat](https://user-images.githubusercontent.com/92692830/200192450-0a911578-1681-4d07-85ab-2050a7216652.png)
