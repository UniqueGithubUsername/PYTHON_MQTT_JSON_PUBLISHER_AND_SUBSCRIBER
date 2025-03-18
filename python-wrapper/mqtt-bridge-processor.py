import json
import paho.mqtt.client as mqtt

broker = 'mqtt.eclipseprojects.io'
port = 1883
topic = 'mqtt_topic'
client_id = 0

def process_message(message):
   print(message)

def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload_in = json.loads(msg.payload)
    print("incoming payload:")
    print(payload_in)

    payload_out = json.dumps(payload_in)
    print("outgoing payload:")
    print(payload_out)

class MQTTBridgeProcessor:
  def __init__(self, broker, port, topic, client_id):
    self.broker = broker
    self.port = port
    self.topic = topic
    self.client_id = client_id
    # MQTT Client
    self.mqttc = mqtt.Client()
    self.mqttc.on_connect = on_connect
    self.mqttc.on_message = on_message

  def __str__(self):
    return f"{self.broker}:{self.port}:{self.topic}:{self.client_id}"

  def connect(self):
    print("Connecting to " + str(self))
    self.mqttc.connect(host=self.broker, port=self.port, keepalive=60)
    self.mqttc.loop_forever()

def main():
  p1 = MQTTBridgeProcessor(broker, port, topic, client_id)
  print(p1)
  p1.connect()

if __name__=="__main__":
  main()