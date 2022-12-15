import psycopg2
import config
import queue_class
import logger_file
import time
import json

import queue_class
from postgre import connection
from postgre import cursor
import logger_file
from postgre_class import db



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
            logger_file.logging.info('no new data found while check')
            continue

def connect_now():
    a = int(input('Update data 1/0?'))
    if a == 1:

        try:
            postgreSQL_select_Query = "SELECT id, topic, payload FROM lpwan.tomqtt;"
            #postgreSQL_select_Query = "SELECT topic, payload from lpwan.mqtt_getqueue()"
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
            logger_file.logging.error('Connection issue while reading from PostgreSQL', exc_info=True)
            print("Connection issue")
            time.sleep(3)
            connect_now()
    else:
        time.sleep(5)
        connect_now()


def setsend(topic, payload):
    #try:
    print(type(topic))
    payload_str = str(payload, 'UTF-8')
    print(type(payload_str))
    query = "SELECT lpwan.mqtt_setsend('"+ topic +"','"+payload_str+"')"
    #print(query)
    #postgreSQL_select_Query = "SELECT lpwan.mqtt_setsend(%s, %s)", str(topic), payload
    cursor.execute(query)
    message = cursor.fetchall()
    print(message)
    #except:
        #print('error')


