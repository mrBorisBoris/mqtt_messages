import psycopg2
import config
import queue_class
import logger_file

queue_to_mqtt = queue_class.Queue_1()


def check_message_to_mqtt():
    try:
        connection = psycopg2.connect(user=config.config['POSTGRE']['user'],
                                      password=config.config['POSTGRE']['password'],
                                      host=config.config['POSTGRE']['host'],
                                      port=config.config['POSTGRE']['port'],
                                      database=config.config['POSTGRE']['database'])
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT topic, payload " \
                                  "FROM lpwan.tomqtt;"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        records = cursor.fetchall()

        print("Print each row and it's columns values")

        for row in records:
            topic = row[0]
            payload = row[1]
            summary = (topic, payload)
            queue_to_mqtt.push(summary)


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        logger_file.logging.error("Ошибка при чтении с PostgreSQL", error, exc_info=True)
        check_message_to_mqtt()



