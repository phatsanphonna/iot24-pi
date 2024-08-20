import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LIGHT = 4

GPIO.setup(LIGHT, GPIO.OUT)
GPIO.cleanup(LIGHT)

