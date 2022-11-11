import ssl

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("Incotex/#")


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)


client = mqtt.Client(client_id="client1", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

# client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)

client.username_pw_set(username="client1", password="aineekeechohdoo7haecah3r")
print("Connecting...")
client.connect("93.188.43.181", 8883)
client.loop_forever()
