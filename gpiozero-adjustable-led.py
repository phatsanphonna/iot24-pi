from gpiozero import MCP3208
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)
pi_pwm = GPIO.PWM(LED_PIN, 1000)
pi_pwm.start(0)

device = MCP3208(channel=7)

while True:
    value = device.value
    voltage = device.voltage

    print(f'Voltage={voltage:.2f}\tValue={value:.2f}')
    pi_pwm.ChangeDutyCycle(int(value * 100))
    sleep(0.1)

