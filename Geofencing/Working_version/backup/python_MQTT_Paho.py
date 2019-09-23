import paho.mqtt.client as mqtt #import the client1
import time
import json


brokers_out={"broker3":"iot.eclipse.org"}
print(brokers_out)
print("brokers_out is a ",type(brokers_out))
print("broker 1 address = ",brokers_out["broker3"])
data_out=json.dumps(brokers_out) # encode oject to JSON

print("\nConverting to JSON\n")
print ("data -type ",type(data_out))
print ("data out =",data_out)

#At Receiver
print("\nReceived Data\n")
data_in=data_out
print ("\ndata in-type ",type(data_in))
print ("data in=",data_in)


brokers_in=json.loads(data_in) #convert incoming JSON to object
print("brokers_in is a ",type(brokers_in))
print("\n\nbroker 1 address = ",brokers_in["broker1"])
cont=input("enter to Continue")


############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

i = 1
while True:
 broker_address="iot.eclipse.org"
 print("creating new instance")
 client = mqtt.Client("P1") #create new instance
 client.on_message=on_message #attach function to callback

 print("connecting to broker")
 client.connect(broker_address) #connect to broker
 client.loop_start() #start the loop

 print("Subscribing to topic","owntracks/geofence/id1")
 client.subscribe("owntracks/geofence/id1") 

 time.sleep(4) # wait
 client.loop_stop() #stop the loop
 i += 1
 print(i)
  

