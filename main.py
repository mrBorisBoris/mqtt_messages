import psycopg2
from psycopg2 import Error
import collections
import time
import paho.mqtt.client as mqtt
import logging
import codecs
import config


logging.basicConfig(level=logging.INFO,
                    filename="py_log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.error('OSError: [Errno 51] Network is unreachable', exc_info=True)
logging.error('--- Logging error ---', exc_info=True)


def postgre_code(record):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="psqlar",
                                      # пароль, который указали при установке PostgreSQL
                                      password="Hgft667rD454w4e",
                                      host="172.20.19.48",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO lpwan.mquery(topic, payload)
                                           VALUES (%s,%s)"""
        # LPWAN = 'Incotex/TEST'
        record_to_insert = ('Incotex/TEST', str(record))

        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно добавлена ​​в таблицy")
        logging.info('Запись успешно добавлена ​​в таблицy')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        logging.error("Ошибка при работе с PostgreSQL", error, exc_info=True)

        postgre_code(record)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
            logging.info('Соединение с PostgreSQL закрыто')





def connection():
    try:
        client.connect("93.188.43.181", 8883)
    except OSError:
        print('Ошибка соединения!')
        time.sleep(1)
        connection()



def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("Incotex/#")


def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    logging.info(msg.topic)
    logging.info(msg.payload)
    queue_to.append(msg.payload)
    data = str(msg.payload, 'UTF-8')
    # print(type(data))
    # print(data)
    record_to = str(data)
    queue_to.popleft()

    # print(data)
    # print(type(data))
    postgre_code(str(record_to))


queue_to = collections.deque()


client = mqtt.Client(client_id="client1", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

client.on_connect = on_connect
client.on_message = on_message



client.username_pw_set(username="client1", password="aineekeechohdoo7haecah3r")
print("Connecting...")
connection()
client.connect("93.188.43.181", 8883)
client.loop_forever()


postgre_code(on_message)

