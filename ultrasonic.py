import RPi.GPIO as GPIO
import time

TRIGGER = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    
    while GPIO.input(ECHO) == 1:
        end_time = time.time()
    
    time_used = end_time - start_time
    distance = time_used * 34300 / 2

    return distance

try:
    while True:
        distance = get_distance()
        print(f'Distance: {distance:.2f}')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()