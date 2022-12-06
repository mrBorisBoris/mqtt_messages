import psycopg2
import config
from psycopg2 import Error

class Postgre_To():
    """Класс отправки данных в постгре"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = self.connection.cursor()













postgre_to = Postgre_To(connection=psycopg2.connect(user=config.config['POSTGRE']['user'],
                                      password=config.config['POSTGRE']['password'],
                                      host=config.config['POSTGRE']['host'],
                                      port=config.config['POSTGRE']['port'],
                                      database=config.config['POSTGRE']['database']))
