import RPi.GPIO as GPIO
import time

BeepPin = 12

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BeepPin, GPIO.OUT)
    GPIO.output(BeepPin, GPIO.HIGH)

def loop():
    while True:
	GPIO.output(BeepPin, GPIO.LOW)
	print 'BEEP LOW'
	time.sleep(0.1)
	GPIO.output(BeepPin, GPIO.HIGH)
	print 'BEEP HIGH'
	time.sleep(0.1)

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
	loop()
    except KeyboardInterrupt:
	destroy()
