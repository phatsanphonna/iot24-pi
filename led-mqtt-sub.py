import paho.mqtt.client as mqtt
from RPi import GPIO

GPIO.setmode(GPIO.BOARD)
LIGHT = 12

GPIO.setup(LIGHT,GPIO.OUT)

HOST = "broker.mqtt-dashboard.com"
TOPIC = "65070171/led2"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode('utf-8')

    print(f'{topic}: {payload}')

    if topic != TOPIC:
        return

    if payload == "ON":
        GPIO.output(LIGHT, True)
    elif payload == "OFF":
        GPIO.output(LIGHT, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, 1883)
client.loop_forever()
