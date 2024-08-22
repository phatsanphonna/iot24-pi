import paho.mqtt.client as mqtt
import time

HOST = "broker.mqtt-dashboard.com"

mqttc = mqtt.Client()
mqttc.connect(HOST, 1883)

while True:
    mqttc.publish("65070171/test/sub", "Hello")
    time.sleep(2)
