import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

BUTTON = 12
HOST = "broker.mqtt-dashboard.com"

GPIO.setup(BUTTON, GPIO.OUT)

mqttc = mqtt.Client()
mqttc.connect(HOST, 1883)

while True:
    value = GPIO.input(BUTTON)
    
    print(value)
    
    if value == 0:
        mqttc.publish("65070171/test/sub2", "ON")
    else:
        mqttc.publish("65070171/test/sub2", "OFF")

    time.sleep(1)
