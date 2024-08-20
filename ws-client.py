import asyncio
import websockets

uri = "ws://192.168.1.35:8765"

async def communicate():
    async with websockets.connect(uri) as websocket:
        message = "hello from client"
        print (f"Send message to server :{message}")
        await websocket.send(message)

        response = await websocket.recv()
        print (f"Recieve Response from server : {response}")


if __name__== "__main__":
        asyncio.run(communicate())
