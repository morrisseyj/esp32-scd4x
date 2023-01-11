#Based on: https://github.com/adafruit/Adafruit_CircuitPython_SCD4X/blob/main/examples/scd4x_simpletest.py
#Copyright (c) 2021 ladyada for Adafruit Industries
#MIT License

import scd4x
import machine
import time

#Create the I2C object
i2c = machine.I2C(0) #use default pins (scl = 18, sda = 19) - to set pins manually see here: https://docs.micropython.org/en/latest/esp32/quickref.html

#Create the sensor object
sensor = scd4x.SCD4X(i2c)

#Begin operating
sensor.start_periodic_measurement()
print("Waiting for first measurement....")

while True:
    if scd4x.data_ready:
        print("CO2: %d ppm" % scd4x.CO2)
        print("Temperature: %0.1f *C" % scd4x.temperature)
        print("Humidity: %0.1f %%" % scd4x.relative_humidity)
        print()
    time.sleep(1)
