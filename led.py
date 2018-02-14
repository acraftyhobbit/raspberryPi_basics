import RPi.GPIO as GPIO
import time

LEDPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LEDPin, GPIO.OUT)
    GPIO.output(LEDPin, GPIO.HIGH)

def loop():
    while True:
        print '...led on!'
	GPIO.output(LEDPin,GPIO.LOW)
	time.sleep(0.5)
	print '...led off'
	GPIO.output(LEDPin, GPIO.HIGH)
	time.sleep(0.5)

def destory():
    GPIO.output(LEDPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
	loop()
    except KeyboardInterrupt:
	destory()
