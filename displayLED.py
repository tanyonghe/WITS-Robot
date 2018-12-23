import time
import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)
device.contrast(5)
virtual = viewport(device, width=32, height=16)
#show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)


def displayLED(val):
	try:
		with canvas(virtual) as draw:
			if val == 0:
				text(draw, (0, 0), "O w O", fill="orange", font=proportional(CP437_FONT))
			if val == 1:
				text(draw, (2, 0), "T n T", fill="orange", font=proportional(CP437_FONT))
			if val == 2:
				text(draw, (0, 0), "^ u ^", fill="orange", font=proportional(CP437_FONT))
			if val == 3:
				text(draw, (2, 0), "> w <", fill="orange", font=proportional(CP437_FONT))
			if val == 4:
				text(draw, (1, 0), "- _ -", fill="orange", font=proportional(CP437_FONT))


	except KeyboardInterrupt:
		GPIO.cleanup()

		
while True:
	displayLED()
	time.sleep(1)