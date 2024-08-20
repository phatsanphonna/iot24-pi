from gpiozero import MCP3208
from time import sleep
from math import log

mcp9700 = MCP3208(channel=0)
termistor = MCP3208(channel=7)

while True:
    mcp9700_temp = 100 * (mcp9700.voltage - 1) + 50

    termistor_resistance = (10000 * termistor.voltage) / (3.3 - termistor.voltage)
    termistor_temp = ((298.15 * 4050) / (298.15 * log(termistor_resistance / 10000) + 4050)) - 273.15

    print(f'MCP9700={mcp9700_temp:.2f}\tThermistor={termistor_temp:.2f}')
    sleep(1)

