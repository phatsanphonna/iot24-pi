import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LIGHT = 8

GPIO.setup(LIGHT,GPIO.OUT)

GPIO.output(LIGHT,True)

time.sleep(3)

GPIO.cleanup()
