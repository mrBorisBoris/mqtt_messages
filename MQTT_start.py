import time
import paho.mqtt.client as mqtt
import logger_file
import postgre
import config
import filter
import sys
import archive_filter
import modem_id_filter

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
            check_modem = msg.topic
            checked = modem_id_filter.filter_modems(check_modem)
            if checked:
                queue_to_global.push([msg.topic, msg.payload])
            else:
                pass




        def push_from_queue():

            if queue_to_global.is_not_empty():
                all_data = queue_to_global.get_data()
                topic = all_data[0]
                payload = str(all_data[1], 'UTF-8')

                if 'Event/Archive' in topic:
                    filtered_data_archive = archive_filter.archive_filter(topic, payload)
                    if filtered_data_archive is not None:
                        print(filtered_data_archive)
                        flag = 'ArchiveNumber2'
                        postgre.postgre_code(filtered_data_archive, flag)

                if 'Events' in topic:

                    filtered_data = filter.data_filter(payload)
                    flag = 'Events'
                    postgre.postgre_code(filtered_data, flag)

                else:
                    record_to_insert = (str(topic), str(payload))
                    flag = False
                    postgre.postgre_code(record_to_insert, flag)


            time.sleep(5)
            push_from_queue()




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
        push_from_queue()
        client.loop_stop()


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
