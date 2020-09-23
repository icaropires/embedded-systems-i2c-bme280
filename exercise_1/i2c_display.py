import time

import smbus2
import bme280

import RPi_I2C_driver

bus = smbus2.SMBus(1)
addr = 0x76
params = bme280.load_calibration_params(bus, addr)

mylcd = RPi_I2C_driver.lcd()
while True:
    try:
        data = bme280.sample(bus, addr, params)

        mylcd.lcd_display_string(f'P={data.pressure:0.2f}', 1)
        mylcd.lcd_display_string(f'U={data.humidity:0.2f}'
                                 f' T={data.temperature:0.2f}', 2)
        time.sleep(1)

    except KeyboardInterrupt:
        break

    finally:
        mylcd.lcd_clear()
        mylcd.backlight(0)
