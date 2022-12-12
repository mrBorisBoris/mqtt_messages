import psycopg2
import config
import queue_class
import logger_file
import time
import json
import threading


def connect_now():
    a = int(input('Update data? 1/0'))
    if a == 1:
        connect()
    else:
        try:
            time.sleep(5)
            connect_now()
        except NameError:
            logger_file.logging.error('Update Error', exc_info=True)
            try_thread.join()


def push_data_to_mqtt(data):
    max_id = 0
    for i_data in data:
        if i_data[0] > max_id:
            max_id = i_data[0]
            data_payload = json.dumps(i_data[2])
            queue_to_mqtt.push((i_data[1], data_payload))
        else:
            time.sleep(5)
            connect()
    time.sleep(5)
    connect()


def selector(cursor):
    postgreSQL_select_Query = "SELECT id, topic, payload " \
                              "FROM lpwan.tomqtt;"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from tomqtt table using cursor.fetchall")
    global data

    data_from = cursor.fetchall()
    return data_from

def update_data(all_data):
    while True:
        time.sleep(5)
        global data
        new_elems = all_data

        for i_elem in new_elems:
            if i_elem not in data:
                print('data append')
                data.append(i_elem)
            else:
                print('data exists')
                #connect_now()
                pass
        print(data)
        return data


def connect():
    try:
        connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                  password=config.config['POSTGRE']['password'],
                                  host=config.config['POSTGRE']['host'],
                                  port=config.config['POSTGRE']['port'],
                                  database=config.config['POSTGRE']['database'])
        cursor = connection.cursor()
        selector(cursor)
        all_messages = update_data(selector(cursor))
        push_data_to_mqtt(all_messages)
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        logger_file.logging.error("Ошибка при чтении с PostgreSQL", error, exc_info=True)


data = []
queue_to_mqtt = queue_class.Queue_1()

try_thread = threading.Thread(target=connect_now(), args=())

