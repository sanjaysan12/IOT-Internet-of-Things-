from gpiozero import LED
from time import sleep
led = LED(17)
while True:
	print("LED turning ON")
	led.on()
	sleep(1)
	print("LED turning OFF")
	led.off()
	sleep(1)
