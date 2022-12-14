import psycopg2
from psycopg2 import Error
import config
import logger_file
import time



def reconnect():
    try:
        connection = psycopg2.connect(database=config.config['POSTGRE']['database'],
                              user=config.config['POSTGRE']['user'],
                              password=config.config['POSTGRE']['password'],
                                 host=config.config['POSTGRE']['host'],
                                 port=config.config['POSTGRE']['port'])
        cursor = connection.cursor()

    except:
        reconnect()


try:
    connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                  # пароль, который указали при установке PostgreSQL
                                  password=config.config['POSTGRE']['password'],
                                  host=config.config['POSTGRE']['host'],
                                  port=config.config['POSTGRE']['port'],
                                  database=config.config['POSTGRE']['database'])
    cursor = connection.cursor()               #необходима проверка на наличие соединения
    if cursor:
         print('Connecting to PostgreSQL...')
    if connection:
         print('Connected to DB.')
         print('Connection status:', connection.status)
except:
    reconnect()
