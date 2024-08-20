import asyncio
import websockets
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LIGHT = 14

GPIO.setup(LIGHT, GPIO.OUT)
GPIO.output(LIGHT, False)

async def echo(websocket, path):
    async for message in websocket:
        print(f"Receive from client : {message}")

        if message == "ON":
            GPIO.output(LIGHT, True)
        else:
            GPIO.output(LIGHT, False)

        await websocket.send(f"Server recieved : {message}")

async def main():
    server = await websockets.serve(echo, "0.0.0.0", 8765)
    print("Server Start,waiting for communication...")
    await server.wait_closed()
    GPIO.cleanup()

if __name__== "__main__":
    asyncio.run(main())

