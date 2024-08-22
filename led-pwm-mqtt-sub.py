import paho.mqtt.client as mqtt
from RPi import GPIO

GPIO.setmode(GPIO.BOARD)
LIGHT = 8

GPIO.setup(LIGHT, GPIO.OUT)

led_pwm = GPIO.PWM(LIGHT, 1000) #create PWM instance with frequency 1000
led_pwm.start(0) #start PWM of 0% Duty Cycle

HOST = "broker.mqtt-dashboard.com"
TOPIC = "65070171/led"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode('utf-8')

    print(f'{topic}: {payload}')

    if topic != TOPIC:
        return

    if payload.upper() == "ON":
        led_pwm.ChangeDutyCycle(100)
    elif payload.upper() == "OFF":
        led_pwm.ChangeDutyCycle(0)
    else:
        led_pwm.ChangeDutyCycle(int(payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, 1883)
client.loop_forever()
