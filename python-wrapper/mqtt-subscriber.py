import json

import paho.mqtt.client as mqtt

broker = 'broker'
port = 1883
topic = 'python/mqtt'
client_id = 0

data = {
    'u1' : [],
    'u2' : [],
    'u3' : [],
    'i1' : [],
    'i2' : [],
    'i3' : [],
    'p1' : [],
    'p2' : [],
    'p3' : [],
    'f' : []
}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    payload_in = json.loads(msg.payload)[1:-1]
    print("incoming payload:")
    print(payload_in)
    vals = payload_in.split(",")
    data['u1'].append(vals[0])
    data['u2'].append(vals[1])
    data['u3'].append(vals[2])
    data['i1'].append(vals[3])
    data['i2'].append(vals[4])
    data['i3'].append(vals[5])
    data['p1'].append(vals[6])
    data['p2'].append(vals[7])
    data['p3'].append(vals[8])
    data['f'].append(vals[9])
    # exchange variable name
    #payload_in['a1'] = payload_in.pop('name')
    print(data)
    #print("outgoing payload:")
    #payload_out = json.dumps(payload_in)
    #print(payload_out)
    #print()
    #client.publish(topic,payload_out)


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()