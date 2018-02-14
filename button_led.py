import RPi.GPIO as GPIO

LedPin = 11
BtnPin = 12

Led_status = 1

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN)
    GPIO.output(LedPin, GPIO.HIGH)

def swLed(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)
    if Led_status == 1:
	print 'Led off!'
    else:
	print 'Led on!'

def loop():
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed)
    while True:
	pass

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
	loop()
    except KeyboardInterrupt:
	destroy()
