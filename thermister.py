import ADC0832
import time

def iniyt():
    ADC0832.setup()

def loop():
    while True:
	res = ADC0832.getResult()
	print 'res = %d' % res
	time.sleep(0.2)

if __name__ == '__main__':
    init()
    try:
	loop()
    except KeyboardInterrupt:
	ADC0832.destory()
	print 'The End'
