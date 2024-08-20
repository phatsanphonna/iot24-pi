import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LIGHT = 4

GPIO.setup(LIGHT,GPIO.OUT)

while True:
    try:
        GPIO.output(LIGHT,True)
    except KeyboardInterrupt:
        GPIO.cleanup()

