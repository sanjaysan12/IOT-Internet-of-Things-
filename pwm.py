import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
channel = 18
GPIO.setup(channel,GPIO.OUT)
p = GPIO.PWM(channel,1)
p.start(1)
i = None
try:
	while i != 'q':
		try:
			f = input("Set a Frequency: ")
			d = input("Set a Duty cycle: ")
			p.ChangeFrequency(int(f))
			p.ChangeDutyCycle(int(d))
			if(d == 'q' or f == 'q'):
				break
		except ValueError as e:
			pass
except KeyboardInterrupt as e:
	print("Received Ctrl+C --> Quitting")
	pass

p.stop()
GPIO.cleanup()
print("I am Exiting")
