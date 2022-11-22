import psycopg2
from psycopg2 import Error
import config
import logger_file
import codecs


def postgre_code(record, topic):
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                      # пароль, который указали при установке PostgreSQL
                                      password=config.config['POSTGRE']['password'],
                                      host=config.config['POSTGRE']['host'],
                                      port=config.config['POSTGRE']['port'],
                                      database=config.config['POSTGRE']['database'])

        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO lpwan.mquery(topic, payload)
                                           VALUES (%s,%s)"""

        record_to_insert = (str(topic), str(record))
        print(record_to_insert)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Запись успешно добавлена в таблицy")
        logger_file.logging.info('Запись успешно добавлена в таблицy')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        logger_file.logging.error("Ошибка при работе с PostgreSQL", error, exc_info=True)

        postgre_code(record, topic)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
            logger_file.logging.info('Соединение с PostgreSQL закрыто')



