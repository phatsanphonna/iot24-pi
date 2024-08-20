from gpiozero import MCP3208
from time import sleep

device = MCP3208(channel=7)

while True:
    voltage = device.voltage

    print(f'Voltage: {voltage}')
    sleep(1)

