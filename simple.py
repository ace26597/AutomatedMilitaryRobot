import RPi.GPIO as GPIO
import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
sensor = Adafruit_DHT.DHT11
pin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mqttc = mqtt.Client('python_pub')
mqttc.connect('broker.hivemq.com', 1883)
gs=0
mn=0
fr=0



while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
    		
		#print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
                ht=str(humidity)+str(temperature)+str(gs)+str(mn)+str(fr)
		print(ht)
		print humidity
		print temperature
		print gs
		print mn
		print fr
		mqttc.publish('/robot',ht)
		mqttc.loop(2)
        	time.sleep(1)
	else:
    		print('Failed to get reading. Try again!')
	gas = GPIO.input(26)
	motion= GPIO.input(4)
	fire=GPIO.input(20)
	
    	if gas == False:
		gs=1
        	time.sleep(0.2)
	else:
		gs=0
		
	if motion == False:
                nm=1
                time.sleep(0.2)
        else:
                mn=0

	
	if fire == False:
		fr=1
	else:
		fr=0
