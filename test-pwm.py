import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) #set pin numbering

ledpin = 8 #PWM pin connected to LED
GPIO.setup(ledpin,GPIO.OUT)

pi_pwm = GPIO.PWM(ledpin,1000) #create PWM instance with frequency 1000
pi_pwm.start(0) #start PWM of 0% Duty Cycle

while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the
        sleep(0.05)