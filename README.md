Micropython library and example for running the Sensirion SCD4X (https://cdn.sparkfun.com/assets/d/4/9/a/d/Sensirion_CO2_Sensors_SCD4x_Datasheet.pdf) sensor on the ESP-WROOM-32 DEVKITV1 (30 pin board). 

Based on https://github.com/adafruit/Adafruit_CircuitPython_SCD4X
Copyright (c) 2021 ladyada for Adafruit Industries
MIT License

&&

Code by Tutaka Kato: https://github.com/mikan/rpi-pico-scd4x
-------------------------------------------------------------------

Note at the time of writing the ESP-WROOM-32 was not supported for circuitpython (https://circuitpython.org/downloads). This microython code has been tested on the SCD40

Wiring as follows (SCD4X : ESP32):
- GND : GND
- VDD : 3V3
- SDA : D19
- SCL : D18

Copy the contents of scd4x.py to the board.

Copy the contents of main.py (example) to the board.

Save and reboot the board.
