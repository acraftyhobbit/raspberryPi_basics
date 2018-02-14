import RPi.GPIO as GPIO
import time

BZRPin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BZRPin, GPIO.OUT)
GPIO.output(BZRPin, GPIO.LOW)

p = GPIO.PWM(BZRPin, 50)
p.start(50)

try:
    while True:
	for f in range(100, 2000, 100):
	    p.ChangeFrequency(f)
	    time.sleep(0.2)

	for f in range(2000, 100, -100):
	    p.ChangeFrequency(f)
	    time.sleep(0.2)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
