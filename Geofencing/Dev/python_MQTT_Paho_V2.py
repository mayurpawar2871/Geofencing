#MQTT Working with broker mqtt.eclipse.org instead of iot.eclipse.org
#JSON decoder reads MQTT msg from broker after subscribing 
#dictionary m_in["batt"] checks for battery level 32 & print status 

import paho.mqtt.client as mqtt #import the client1
import time
import json


brokers_out={"broker2":"mqtt.eclipse.org"}
print(brokers_out)
print("brokers_out is a ",type(brokers_out))
print("broker 2 address = ",brokers_out["broker2"])



############
def on_message(client, userdata, msg):
    #print("message topic=",msg.topic)
    #print("message qos=",msg.qos)
    #print("message retain flag=",msg.retain)

    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    m_in=json.loads(m_decode) #decode json data
    #print(type(m_in))
    print("ACTUAL DATA = ",m_in["batt"])
    if m_in["batt"] == 32:
     print("BATTERY FULL")
    else:
     print("BATTERY EMPTY")
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

 print("Subscribing to topic","owntracks/geofence/id1")
 client.subscribe("owntracks/geofence/id1") 

 time.sleep(4) # wait
 client.loop_stop() #stop the loop
 i += 1
 print("ATTEMPT",i)
  

