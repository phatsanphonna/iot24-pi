import paho.mqtt.client as mqtt
from gpiozero import MCP3208
import time

HOST = "broker.mqtt-dashboard.com"
TOPIC = "65070171/adjustable-resistor"

device = MCP3208(channel=0)

mqttc = mqtt.Client()
mqttc.connect(HOST, 1883)

while True:
    mqttc.publish(TOPIC, str(device.voltage))
    time.sleep(2)
