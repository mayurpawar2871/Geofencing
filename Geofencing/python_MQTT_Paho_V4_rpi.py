#MQTT Working with broker mqtt.eclipse.org instead of iot.eclipse.org
#JSON decoder reads MQTT msg from broker after subscribing 
#dictionary m_in["batt"] checks for battery level 32 & print status 
# 31 oct , timlong is to move RPI
# If lattitude long is 35.717 then using import dec , trim funtion extracted only 717 value
# Feb 9 COMPLETED ,Working with ON/OFF FAN when leaves from home & come at home


import paho.mqtt.client as mqtt #import the client1
import time
import json
import os
import subprocess
import decimal

brokers_out={"broker2":"mqtt.eclipse.org"}
print(brokers_out)
#print("brokers_out is a ",type(brokers_out))
#print("broker 2 address = ",brokers_out["broker2"])


def trim_func(variable):
    temp = int(variable)
    variable =variable - temp
    variable =variable*1000
    variable =int(variable)
    return variable;

############
def on_message(client, userdata, msg):
    #print("message topic=",msg.topic)
    #print("message qos=",msg.qos)
    #print("message retain flag=",msg.retain)

    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("data Received type",type(m_decode))
    #print("data Received",m_decode)
    #print("Converting from Json to Object")
    m_in=json.loads(m_decode) #decode json data
    #print(type(m_in))
    print("ACTUAL DATA = ",m_in["batt"])
    batt= m_in["batt"]
    Lattitude=m_in["lat"]
    Lattitude=35.71723
    Lattitude=trim_func(Lattitude);
    Longitude=m_in["lon"]
    #Longitude=139.96923
    Longitude=trim_func(Longitude);
    print("Battery=",batt)
    print("Lattitude",Lattitude)
    print("Longitude",Longitude) 
    if (Lattitude == 717 and  
       Longitude == 969 or Longitude == 968 ):
     print("YOU ARE AT HOME")
     os.system('sudo ./uhubctl -l 1-1 -p 2 -a on ')  
    else:
     print("NOT AT HOME")
     os.system('sudo ./uhubctl -l 1-1 -p 2 -a off ')
########################################
#  format '{"_type":"location","acc":15,"alt":77,"batt":39,"conn":"w","inregions":["home"],"lat":35.7175005,"lon":139.9688588,"t":"u","tid":"ge","tst":1569174818,"vac":2,"vel":0}')

broker_address="mqtt.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

i = 1
while True:
 client.loop_start() #start the loop

 #print("Subscribing to topic","owntracks/geofence/id1")
 client.subscribe("owntracks/geofence/id1") 

 time.sleep(4) # wait
 client.loop_stop() #stop the loop
 i += 1
 print("ATTEMPT",i)
  

