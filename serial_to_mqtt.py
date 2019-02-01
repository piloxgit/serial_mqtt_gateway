import serial
import paho.mqtt.client as mqttClient
import time

serialdev = '/dev/ttyUSB0'
broker_address= "localhost"
port = 1883

try:
    print("Connecting to serial... "), serialdev
    ser = serial.Serial(serialdev, 115200, timeout=20)
    print("Connected to serial")

except:
    print("Failed to connect serial")
    raise SystemExit

while 1:
    line = ser.readline()
    print (line)
    client = mqttClient.Client("Python")             
    client.connect(broker_address, port=port)        
    client.publish("teplota",line)
    
