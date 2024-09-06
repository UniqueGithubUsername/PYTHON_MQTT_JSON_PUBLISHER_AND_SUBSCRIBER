import time
import json

import paho.mqtt.client as mqtt

broker = 'broker'
port = 1883
topic = 'python/mqtt'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = '{ "name":"John", "age":' + str(msg_count) + ', "city":"New York"}'
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

mqttc.loop_start()
publish(mqttc)
mqttc.loop_stop()