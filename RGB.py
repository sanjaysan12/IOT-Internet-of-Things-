import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
channel = [13,19,12]
for c in channel:

	GPIO.setup(c,GPIO.OUT)
	p = GPIO.PWM(c,10)


p.start(30)
try:
	while True:
		try:
			i = input("Enter a number between 0-7: ")
			i = int(i)
			if (i < 0 or i >= 8):
				print("Invalid range of input.... Try Again...")
				continue
			rgb = format(i,'03b')
			for i,c in enumerate(channel):
				print(i,c,rgb[i])
				GPIO.output(c,not bool(int(rgb[i])))
		except ValueError:
			print("Invalid input try again")

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Quitting")