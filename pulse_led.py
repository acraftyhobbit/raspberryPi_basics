import RPi.GPIO as GPIO
import time

LedPin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.LOW)

p = GPIO.PWM(LedPin, 1000)
p.start(0)

try:
    while True:
	for dc in range(0, 101, 4):
	    p.ChangeDutyCycle(dc)
	    time.sleep(0.5)
	time.sleep(1)
	for dc in range(100, -1, -4):
	    p.ChangeDutyCycle(dc)
	    time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()
