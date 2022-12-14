import time
import paho.mqtt.client as mqtt
import logger_file
import config
import sys
import modem_id_filter
import postgre_get_data
import queue_class
#import psycopg_test

sys.setrecursionlimit(2000000)


class  Data_MQTT():
    """Общий класс входящей информации"""
    def __init__(self, topic, payload):
        self.topic = str(topic)
        self.payload = str(payload, 'UTF-8')

class MQTT():
    """Общий класс объекта клиента"""
    def __init__(self, client):
        self.client = mqtt.Client(client_id="client1",
                                  clean_session=True,
                                  userdata=None,
                                  protocol=mqtt.MQTTv311,
                                  transport="tcp")


    def MQTT_start(self):
        """Запуск клиента"""

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
            checked = modem_id_filter.filter_modems(msg.topic)
            if checked:
                queue_to_global.push([msg.topic, msg.payload])
            else:
                pass

        def on_publish(client, userdata, result):
            print('data published')

        def push_from_postgre():
            if queue_to_push.is_not_empty():
                data_from = queue_to_push.get_data()
                topic = str(data_from[0])
                payload = data_from[1]
                data_typle = (topic, payload)
                if data_typle not in data_list:
                    data_list.append(data_typle)
                    print('new data')
                    ret = client.publish(topic, payload)
                    print(ret)
                if data_typle in data_list:
                    print('data exists')
                # ret = client.publish(topic, payload)
                push_from_postgre()

        def push_from_mqtt_to_postgre():
            if queue_to_global.is_not_empty():
                queue_to_global.data_filter()

            time.sleep(5)
            push_from_mqtt_to_postgre()




        client = mqtt.Client(client_id="client1",
                                  clean_session=True,
                                  userdata=None,
                                  protocol=mqtt.MQTTv311,
                                  transport="tcp")
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_publish = on_publish

        client.username_pw_set(username='client1',
                               password='aineekeechohdoo7haecah3r')
        print("Connecting...")
        connection()
        client.connect(config.config['MQTT']['host'], int(config.config['MQTT']['port']))
        queue_to_push = postgre_get_data.queue_to_mqtt
        data_list = []
        if queue_to_push.is_not_empty():
            print('data here')
        else:
            print('no data')

        client.loop_start()
        queue = queue_class.Queue_1()
        push_from_postgre()
        push_from_mqtt_to_postgre() # Вызываем функцию на фильтрацию очереди и отправку данных
        client.loop_stop()


queue_to_global = queue_class.Queue_1()


