# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import os

def on_connect(client, userdata, rc):
        print ('Connected with result code '+str(rc))

        client.subscribe('/Led')


def on_message(client, userdata, msg):
        print 'Topic: ', msg.topic + '\n' 'Message:' +str(msg.payload)
        if "for" in msg.payload:
                print "forword"
                os.system("sudo gpio -g write 5 1")
                os.system("sudo gpio -g write 6 0")
                os.system("sudo gpio -g write 13 1")
                os.system("sudo gpio -g write 19 0")
        if "rev" in msg.payload:
                print "Reverse"
                os.system("sudo gpio -g write 5 0")
                os.system("sudo gpio -g write 6 1")
                os.system("sudo gpio -g write 13 0")
                os.system("sudo gpio -g write 19 1")
        if "left" in msg.payload:
                print "Left"
                os.system("sudo gpio -g write 5 0")
                os.system("sudo gpio -g write 6 1")
                os.system("sudo gpio -g write 13 1")
                os.system("sudo gpio -g write 19 0")
        if "right" in msg.payload:
                print "Right"
                os.system("sudo gpio -g write 5 1")
		os.system("sudo gpio -g write 6 0")
                os.system("sudo gpio -g write 13 0")
                os.system("sudo gpio -g write 19 1")

        if "stop" in msg.payload:
                print "stop"
                os.system("sudo gpio -g write 5 0")
                os.system("sudo gpio -g write 6 0")
                os.system("sudo gpio -g write 13 0")
                os.system("sudo gpio -g write 19 0")
        if "low" in msg.payload:
                print "Low"
                os.system("sudo gpio pwm 1 1023")
        if "ledon" in msg.payload:
                print "Light on"
                os.system("sudo gpio -g write 4 1")
        if "ledoff" in msg.payload:
                print "Light Off"
                os.system("sudo gpio -g write 4 0")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('broker.hivemq.com', 1883, 60)
client.loop_forever()


