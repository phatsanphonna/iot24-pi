from gpiozero import MCP3208
from time import sleep

device = MCP3208(channel=0)

while True:
    voltage = device.voltage

    print(f'Voltage: {voltage}')
    sleep(1)

