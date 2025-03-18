import time
import random
import json

from datetime import datetime

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
        #msg = '{ "time":"' + str(datetime.now()) + '", "value":"' + str(msg_count) + '"}'
        # Add random values within realistic measurement boundaries
        msg = [
            # Voltage: 227.0 - 235.0 V
            *[
                complex(
                    random.uniform(227.0, 235.0), random.uniform(0.0, 11.5)
                )
                for _ in range(3)
            ],
            # Current: 0.0 - 1.15 A
            *[
                complex(
                    random.uniform(22.7, 23.5), random.uniform(0.0, 1.5)
                )
                for _ in range(3)
            ],
            # Power: 0.95 - 1.0
            *[
                complex(
                    random.uniform(5152.9, 5522.5),
                    random.uniform(0.0, 17.25),
                )
                for _ in range(3)
            ],
            # Frequency: 49.9 - 50.1 Hz
            random.uniform(49.9, 50.1),
        ]

        result = client.publish(topic, json.dumps(str(msg)))
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        #if msg_count > 5:
        #    break

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

mqttc.loop_start()
publish(mqttc)
mqttc.loop_stop()