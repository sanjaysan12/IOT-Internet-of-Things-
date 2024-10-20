import RPi.GPIO as GPIO
from time import sleep

class RGBA():
	
	def __init__(self, r,g,b):
		GPIO.setmode(GPIO.BCM)
		channel = [r,g,b]
		for c in channel:
			GPIO.setup(c , GPIO.OUT)
		self.r = GPIO.PWM(r,120)
		self.g = GPIO.PWM(g,120)
		self.b = GPIO.PWM(b,120)
		self.r.start(0)
		self.g.start(0)
		self.b.start(0)

	def setcolor(self,r,g,b):
		r = 100 - (r / 255) * 100
		g = 100 - (g / 255) * 100
		b = 100 - (b / 255) * 100
		print(r,g,b)
		self.r.ChangeDutyCycle(int(r))
		self.g.ChangeDutyCycle(int(g))
		self.b.ChangeDutyCycle(int(b))

led = RGBA(13,19,12)
try:
	while True:
		r = input("Enter clour for r: ")
		g = input("Enter clour for g: ")
		b = input("Enter clour for b: ")
		if r == 'q' or g == 'q' or b == 'q':
			print("Received Quit... So Quitting..")
			break	
		
		led.setcolor(int(r),int(g),int(b))
		sleep(1)
		
except KeyboardInterrupt:
	print("Received Ctrl + C Quitting...")
GPIO.cleanup()

