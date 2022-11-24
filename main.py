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


class  Data_MQTT():
    """Общий класс входящей информации"""
    def __init__(self, topic, payload):
        self.topic = str(topic)
        self.payload = str(payload, 'UTF-8')

class MQTT():
    def __init__(self, client):
        self.client = mqtt.Client(client_id="client1",
                                  clean_session=True,
                                  userdata=None,
                                  protocol=mqtt.MQTTv311,
                                  transport="tcp")


    def MQTT_start(self):

        def connection():
            try:
                client.connect(config.config['MQTT']['host'], int(config.config['MQTT']['port']))
            except OSError:
                logger_file.logging.error('OSError: [Errno 51] Network is unreachable', exc_info=True)
                print('Ошибка соединения!')
                time.sleep(1)
                connection()

        def on_connect(client, userdata, flags, rc):
            print("Connected with result code", rc)
            client.subscribe("Incotex/#")

        def on_message(client, userdata, msg):
            queue_to_global.push([msg.topic, msg.payload])

        def is_empty():
            print(queue_to_global.is_not_empty())
            if queue_to_global.is_not_empty():
                all_data = queue_to_global.get_data()
                topic = all_data[0]
                payload = str(all_data[1], 'UTF-8')

                if 'Events' not in topic:
                    record_to_insert = (str(topic), str(payload))
                    flag = False
                    postgre.postgre_code(record_to_insert, flag)
                else:
                    filtered_data = filter.data_filter(payload)
                    flag = True
                    postgre.postgre_code(filtered_data, flag)


            time.sleep(5)
            is_empty()




        client = mqtt.Client(client_id="client1",
                                  clean_session=True,
                                  userdata=None,
                                  protocol=mqtt.MQTTv311,
                                  transport="tcp")
        client.on_connect = on_connect
        client.on_message = on_message

        client.username_pw_set(username='client1',
                               password='aineekeechohdoo7haecah3r')
        print("Connecting...")
        connection()
        client.connect('93.188.43.181', 8883)

        client.loop_start()
        is_empty()



class Queue_1():
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def get_data(self):
        return self.queue.pop(0)

    def is_not_empty(self):
        if len(self.queue) != 0:
            return True
        else:
            return False







queue_to_global = Queue_1()
MQTT_starter = MQTT(client=mqtt.Client(client_id="client1",
                                  clean_session=True,
                                  userdata=None,
                                  protocol=mqtt.MQTTv311,
                                  transport="tcp"))

MQTT_starter.MQTT_start()


