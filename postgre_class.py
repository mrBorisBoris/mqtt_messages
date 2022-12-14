import psycopg2
import config
from psycopg2 import Error
import logger_file
import time
import json

def reconnect():
    try:
        connection = psycopg2.connect(database=config.config['POSTGRE']['database'],
                                           user=config.config['POSTGRE']['user'],
                                           password=config.config['POSTGRE']['password'],
                                           host=config.config['POSTGRE']['host'],
                                           port=config.config['POSTGRE']['port'])
        cursor = connection.cursor()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

class Postgre_To():
    def __init__(self, database=config.config['POSTGRE']['database'],
                 user=config.config['POSTGRE']['user'],
                 password=config.config['POSTGRE']['password'],
                 host=config.config['POSTGRE']['host'], port=config.config['POSTGRE']['port']):
        self.connection = psycopg2.connect(database=database,
                                   user=user,
                                   password=password,
                                   host=host,
                                   port=port)
        self.cursor = self.connection.cursor()
    def check_connection(self):
        print(db.connection)
        print(db.cursor)
        print(db.connection.status)
    def insert_into(self, record, flagged):
        try:
            if not flagged:
                record_to_insert = record
                print(record_to_insert)

                postgres_insert_query = """ INSERT INTO lpwan.mquery(topic, payload)
                                                   VALUES (%s,%s)"""

                self.cursor.execute(postgres_insert_query, record_to_insert)

                self.connection.commit()
                count = self.cursor.rowcount  # сделать отдельным методом в классе проверку

                print(count, "Запись успешно добавлена в таблицy mquery")
                logger_file.logging.info('Запись успешно добавлена в таблицy')

            if flagged == 'ArchiveNumber2':
                record_to_insert = record
                print(record_to_insert)
                postgres_insert_query = """ INSERT INTO lpwan.devdaily(modem_id, act, act1, act2, react, act_minus, react_minus, devtime, devdata)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

                self.cursor.execute(postgres_insert_query, record_to_insert)
                self.connection.commit()
                count = self.cursor.rowcount
                print(count, "Запись успешно добавлена в таблицy dev_daily")
                logger_file.logging.info('Запись успешно добавлена в таблицy dev_daily')

            if flagged == 'Events':
                record_to_insert = record
                print(record_to_insert)

                postgres_insert_query = """ INSERT INTO lpwan.events(modem_id, ev_time, ev_code, ev_type, journal)
                                                               VALUES (%s,%s,%s,%s,%s)"""

                self.cursor.execute(postgres_insert_query, record_to_insert)
                self.connection.commit()
                count = self.cursor.rowcount
                print(count, "Запись успешно добавлена в таблицy events")
                logger_file.logging.info('Запись успешно добавлена в таблицy events')

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            logger_file.logging.error("Ошибка при работе с PostgreSQL", error, exc_info=True)
            time.sleep(5)
            reconnect()



db = Postgre_To()
#db.insert_into((str('Incotex/TEST'), str(json.dumps('{CommandParams: 123}'))), False)


