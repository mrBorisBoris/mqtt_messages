import configparser
import os
import paho.mqtt.client as mqtt
import time
import logging

logging.basicConfig(level=logging.INFO,
                    filename="py_log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.error('OSError: [Errno 51] Network is unreachable', exc_info=True)
logging.error('--- Logging error ---', exc_info=True)


def connection():
    try:
        client.connect("93.188.43.181", 8883)
    except OSError:
        print('Ошибка соединения!')
        time.sleep(1)
        connection()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("Incotex/#")


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    logging.info(msg.topic)
    logging.info(msg.payload)


client = mqtt.Client(client_id="client1", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

# client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)

client.username_pw_set(username="client1", password="aineekeechohdoo7haecah3r")
print("Connecting...")
connection()
client.connect("93.188.43.181", 8883)
client.loop_forever()
