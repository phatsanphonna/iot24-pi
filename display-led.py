# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# SHT31
# This code is designed to work with the SHT31_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Humidity?sku=SHT31_I2CS#tabs-0-product_tabset-2

from smbus3 import SMBus
from rpi_lcd import LCD
import time

# Get I2C bus
bus = SMBus(1)
lcd = LCD(0x27)

# SHT31 address, 0x44(68)
# Send measurement command, 0x2C(44)
#		0x06(06)	High repeatability measurement
bus.write_i2c_block_data(0x44, 0x2C, [0x06])

time.sleep(0.5)

# SHT31 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data = bus.read_i2c_block_data(0x44, 0x00, 6)

# Convert the data
temp = data[0] * 256 + data[1]
cTemp = -45 + (175 * temp / 65535.0)
fTemp = -49 + (315 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

# Output data to screen
print("Temperature in Celsius is : %.2f C" % cTemp)
print("Temperature in Fahrenheit is : %.2f F" % fTemp)
print("Relative Humidity is : %.2f %%RH" % humidity)

lcd.text(f"Temp: {cTemp:.2f} C", 1)
lcd.text(f"Humi: {humidity:.2f}%", 2)