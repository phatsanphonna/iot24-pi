import asyncio
import websockets
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #set pin numbering

ledpin = 8 #PWM pin connected to LED
GPIO.setup(ledpin,GPIO.OUT)

uri = "ws://10.30.6.54:8765"

pi_pwm = GPIO.PWM(ledpin, 1000)
pi_pwm.start(0)

async def communicate():
    async with websockets.connect(uri) as websocket:
        while True:
            response = await websocket.recv()
            print(f"Recieve Response from server : {response}")
            pi_pwm.ChangeDutyCycle(float(response))


if __name__== "__main__":
        asyncio.run(communicate())
