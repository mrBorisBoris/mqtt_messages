import psycopg2
from psycopg2 import Error
import config
import logger_file




def postgre_code(record, flagged):
    try:
        # Подключиться к существующей базе данных
        #connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                      # пароль, который указали при установке PostgreSQL
        #                              password=config.config['POSTGRE']['password'],
        #                              host=config.config['POSTGRE']['host'],
        #                              port=config.config['POSTGRE']['port'],
        #                              database=config.config['POSTGRE']['database'])

        #cursor = connection.cursor()

        if not flagged:
            record_to_insert = record
            print(record_to_insert)

            postgres_insert_query = """ INSERT INTO lpwan.mquery(topic, payload)
                                           VALUES (%s,%s)"""

            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount  #сделать отдельным методом в классе проверку

            print(count, "Запись успешно добавлена в таблицy mquery")
            logger_file.logging.info('Запись успешно добавлена в таблицy')

        if flagged == 'ArchiveNumber2':
            record_to_insert = record
            print(record_to_insert)
            postgres_insert_query = """ INSERT INTO lpwan.devdaily(modem_id, act, act1, act2, react, act_minus, react_minus, devtime,  devdata)
            VALUES (%s,%s,s%,s%,s%,s%,s%,s%,s%')"""

            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, "Запись успешно добавлена в таблицy dev_daily")
            logger_file.logging.info('Запись успешно добавлена в таблицy dev_daily')

        if flagged == 'Events':
            record_to_insert = record
            print(record_to_insert)

            postgres_insert_query = """ INSERT INTO lpwan.events(modem_id, ev_time, ev_code, ev_type, journal)
                                                       VALUES (%s,%s,%s,%s,%s)"""

            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            print(count, "Запись успешно добавлена в таблицy events")
            logger_file.logging.info('Запись успешно добавлена в таблицy events')




    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        logger_file.logging.error("Ошибка при работе с PostgreSQL", error, exc_info=True)
        postgre_code(record, flagged)




connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                  # пароль, который указали при установке PostgreSQL
                                  password=config.config['POSTGRE']['password'],
                                  host=config.config['POSTGRE']['host'],
                                  port=config.config['POSTGRE']['port'],
                                  database=config.config['POSTGRE']['database'])
cursor = connection.cursor()
if cursor:
    print('ok')
if connection:
    print('connect ok')
    print(connection.status)