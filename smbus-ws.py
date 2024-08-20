import asyncio
import websockets
from smbus3 import SMBus
import time

uri = "ws://192.168.1.35:8765"

# Get I2C bus
bus = SMBus(1)

# SHT31 address, 0x44(68)
# Send measurement command, 0x2C(44)
#		0x06(06)	High repeatability measurement
bus.write_i2c_block_data(0x44, 0x2C, [0x06])

async def communicate():
    async with websockets.connect(uri) as websocket:
        data = bus.read_i2c_block_data(0x44, 0x00, 6)

        # Convert the data
        temp = data[0] * 256 + data[1]
        cTemp = -45 + (175 * temp / 65535.0)

        await websocket.send(str(cTemp))

        response = await websocket.recv()
        print(f"Recieve Response from server : {response}")


if __name__== "__main__":
        asyncio.run(communicate())
