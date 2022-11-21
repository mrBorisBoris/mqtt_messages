import psycopg2
from psycopg2 import Error
import collections
import time
import logging
import codecs


logging.basicConfig(level=logging.INFO,
                    filename="py_log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.error('OSError: [Errno 51] Network is unreachable', exc_info=True)
logging.error('--- Logging error ---', exc_info=True)


def postgre_code(record, topic):
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
        record_to_insert = (str(topic), str(record))
        print(record_to_insert)
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



