import time
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def cb(smp):
    print(smp)


def main():
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    topic = "data/measurements/demo-data"
    port = 8080
    mqttc.connect(topic, port, 60)
    mqttc.loop_forever()

    data = [
        (234.0500030517578 + 5.555959224700928j),
        (231.57659912109375 + 9.166434288024902j),
        (233.78140258789062 + 2.692197799682617j),
        (23.3004150390625 + 0.8415144085884094j),
        (22.90943145751953 + 0.9212493896484375j),
        (22.97486114501953 + 0.30015939474105835j),
        (5345.9091796875 + 7.389429569244385j),
        (5427.345703125 + 3.168224573135376j),
        (5452.58447265625 + 6.7838454246521j),
        49.905172231139446,
    ]

    last_block = datetime.now()
    block_interval = timedelta(seconds=2)

    i = 0
    while i < 10:
        print(i)

        if datetime.now() - last_block > block_interval:
            smp = Sample(data=data)
            print("CB:")
            cb(smp)
            last_block = datetime.now()

        for x, _ in enumerate(data):
            data[x] += 0.1 * random.uniform(-1, 1)

        time.sleep(1.0)
        i = i + 1


if __name__ == "__main__":
    main()
