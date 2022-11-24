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
import filter

from queue import Queue
global_data = ''
msg_topic = None
msg_payload = None
if msg_payload != None:
    print('GLOBAL', msg_payload)
    print('GLOBAL', msg_topic)


class  Data_MQTT():
    """Общий класс входящей информации"""
    def __init__(self, topic, payload):
        self.topic = str(topic)
        self.payload = str(payload, 'UTF-8')



class Queue_1():
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


def global_update(data):
    print('GLOBAL', data)
    time.sleep(1)
    global_update(data)



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
    q.put([data_mqtt.topic, data_mqtt.payload])
    new_data_object = q.get()
    data_topic = new_data_object[0]
    data_payload = new_data_object[1]

    """Подключение модуля фильтрации к Events"""
    if 'Events' not in data_topic:
        record_to_insert = (str(data_topic), str(data_payload))
        flag = False
        postgre.postgre_code(record_to_insert, flag)

    else:
        filtered_data = filter.data_filter(data_mqtt.payload)
        flag = True
        record_to_insert = filtered_data
        postgre.postgre_code(record_to_insert, flag)
        print(filtered_data)





queue_to = Queue_1()

if msg_payload != None:
    print('GLOBAL', msg_payload)
    print('GLOBAL', msg_topic)
if msg_topic != None:
    print('it works')


q = Queue()
if not q.empty():
    print(q.get())

print(global_data)




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




