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
    for i_data in data:
        data_payload = json.dumps(i_data[1])
        print(i_data[0], data_payload)
        queue_to_mqtt.push((i_data[0], data_payload))


def connect_now():
    a = 1
    if a == 1:

        try:
            #postgreSQL_select_Query = "SELECT id, topic, payload FROM lpwan.tomqtt;"
            #postgreSQL_select_Query = "with lst as (select min(timestmp) as timestmp, modem_id FROM lpwan.tomqtt " \
            #                          "where complete is null and CURRENT_TIMESTAMP-timestmp < interval '1 hours'" \
            #                          "group by modem_id)" \
            #                          "SELECT  topic, payload " \
            #                          "FROM lst" \
            #                          "join lpwan.tomqtt m on m.modem_id=lst.modem_id and m.timestmp=lst.timestmp" \
            #                          "where sended is null"
            postgreSQL_select_Query = "SELECT topic, payload FROM lpwan.mqtt_que"
            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from tomqtt table using cursor.fetchall")
            all_messages = cursor.fetchall()
            connection.commit()
            global data
            create_query_to_mqtt(data)
            data = all_messages
            print(data)
            time.sleep(15)
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
    payload_str = str(payload, 'UTF-8')
    query = "SELECT lpwan.mqtt_setsend('" + topic + "','" + payload_str + "')"
    print(query)
    try:
        cursor.execute(query)
        connection.commit()
        print('setsend ok')
    except:
        pass


def setanswer(topic, payload):
    payload_to = str(payload, 'UTF-8')

    query = "SELECT lpwan.mqtt_setanswer('" + topic + "','" + payload_to + "')"
    print(query)
    cursor.execute(query)
    connection.commit()
    print('setanswer ok')


