import psycopg2
import config
from psycopg2 import Error



class Postgre_To:
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


db = Postgre_To()
db.check_connection()