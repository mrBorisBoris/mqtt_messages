import psycopg2
import config
import queue_class
import logger_file
import schedule
import time
import threading
import json

queue_to_mqtt = queue_class.Queue_1()
count = 0
data = []

def check_message_to_mqtt():
        try:
            connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                      password=config.config['POSTGRE']['password'],
                                      host=config.config['POSTGRE']['host'],
                                      port=config.config['POSTGRE']['port'],
                                      database=config.config['POSTGRE']['database'])
            cursor = connection.cursor()
            postgreSQL_select_Query = "SELECT id, topic, payload " \
                                  "FROM lpwan.tomqtt;"

            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from tomqtt table using cursor.fetchall")
            global data

            data = cursor.fetchall()





        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            logger_file.logging.error("Ошибка при чтении с PostgreSQL", error, exc_info=True)
            check_message_to_mqtt()


check_message_to_mqtt()
max_id = 0
for i_data in data:
    if i_data[0] > max_id:
        max_id = i_data[0]
        data_payload = json.dumps(i_data[2])
        queue_to_mqtt.push((i_data[1], data_payload))
    else:
        pass




