import psycopg2
from psycopg2 import Error
import collections
import time
import paho.mqtt.client as mqtt
import logger_file
import postgre
import codecs
import config


class  Data_MQTT():
    """Общий класс входящей информации"""
    def __init__(self, topic, payload):
        self.topic = str(topic)
        self.payload = str(payload, 'UTF-8')

        # if 'Events' in topic:
            # self.topic = 'LPWAN/Events'
        # if 'MeterState' in topic:
            # self.topic = 'LPWAN/MeterState'
        # if 'Archive' in topic:
            # self.topic = 'LPWAN/Archive'
        # if 'MeterPassport' in topic:
            # self.topic = 'LPWAN/MeterPassport'
        #elif 'Instants' in topic:
           # self.topic = 'LPWAN/Instants'


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
    # print(msg.topic, msg.payload)
    data_mqtt = Data_MQTT(msg.topic, msg.payload)

    # logger_file.logging.info(msg.topic)
    # logger_file.logging.info(msg.payload)
    queue_to.append(msg.payload)
    topic_to_record = data_mqtt.topic
    # print(data_mqtt.topic)
    record_to = data_mqtt.payload
    queue_to.popleft()
    postgre.postgre_code(record_to, topic_to_record)


queue_to = collections.deque()


client = mqtt.Client(client_id="client1",
                     clean_session=True,
                     userdata=None,
                     protocol=mqtt.MQTTv311,
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set(username=config.config['MQTT']['user'],
                       password=config.config['MQTT']['password'])
print("Connecting...")
connection()
client.connect(config.config['MQTT']['host'], int(config.config['MQTT']['port']))
client.loop_forever()




