import psycopg2
from psycopg2 import Error
import collections
import time
import paho.mqtt.client as mqtt
import logger_file
import postgre
import codecs
import config
import json


class  Data_MQTT():
    """Общий класс входящей информации"""
    def __init__(self, topic, payload):
        self.topic = str(topic)
        self.payload = str(payload, 'UTF-8')



class Queue():
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def get_topic(self):
        return self.queue.pop(0)

    def get_payload(self):
        return self.queue.pop(0)

    def is_not_empty(self):
        if len(self.queue) != 0:
            return True
        else:
            return False
    def whats_in(self):
        return self.queue





def connection():
    try:
        client.connect("93.188.43.181", 8883)
    except OSError:
        logger_file.logging.error('OSError: [Errno 51] Network is unreachable', exc_info=True)
        print('Ошибка соединения!')
        time.sleep(1)
        connection()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("Incotex/#")


def on_message(client, userdata, msg):
    data_mqtt = Data_MQTT(msg.topic, msg.payload)
    if data_mqtt.topic:
        queue_to.push(data_mqtt.topic)
    if data_mqtt.payload:
        queue_to.push(data_mqtt.payload)

    if queue_to.is_not_empty():
        record_to_insert = (str(queue_to.get_topic()), str(queue_to.get_payload()))
        postgre.postgre_code(record_to_insert)



queue_to = Queue()







client = mqtt.Client(client_id="client1",
                     clean_session=True,
                     userdata=None,
                     protocol=mqtt.MQTTv311,
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message
# if queue_to.is_not_empty():
#   print(queue_to.whats_in())
#    topic_to_push = queue_to.get_topic()
#
#    payload_to_push = queue_to.get_payload()
#
#    postgre.postgre_code(payload_to_push, topic_to_push)



client.username_pw_set(username=config.config['MQTT']['user'],
                       password=config.config['MQTT']['password'])
print("Connecting...")
connection()
client.connect(config.config['MQTT']['host'], int(config.config['MQTT']['port']))
client.loop_forever()




