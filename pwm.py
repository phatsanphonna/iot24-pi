import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

ledpin = 12
GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)
pi_pwm.start(0)

while True:
    for duty in range(0,101,1):
        print('Running ' + str(duty))
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.05)