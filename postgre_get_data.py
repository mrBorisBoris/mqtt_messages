import psycopg2
import config
import queue_class
import logger_file
import time
import json
import threading
import queue_class
import MQTT_start

data = []
queue_to_mqtt = queue_class.Queue_1()
data_to_check = []

def create_query_to_mqtt(data):
    global queue_to_mqtt
    max_id = 0
    for i_data in data:
        if i_data[0] > max_id:
            max_id = i_data[0]
            data_payload = json.dumps(i_data[2])
            print(i_data[1], data_payload)
            queue_to_mqtt.push((i_data[1], data_payload))


        else:
            pass

def connect_now():
    a = int(input('Update data 1/0?'))
    if a == 1:
        try:
            connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                          password=config.config['POSTGRE']['password'],
                                          host=config.config['POSTGRE']['host'],
                                          port=config.config['POSTGRE']['port'],
                                          database=config.config['POSTGRE']['database'])
            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT id, topic, payload FROM lpwan.tomqtt;"
            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from tomqtt table using cursor.fetchall")
            all_messages = cursor.fetchall()
            global data
            create_query_to_mqtt(data)
            data = all_messages
            print(data)
            time.sleep(5)
            connect_now()


        except:
            print("Connection issue")
            time.sleep(3)
            connect_now()
    else:
        time.sleep(5)
        connect_now()




