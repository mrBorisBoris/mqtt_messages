import threading
import psycopg_test
import MQTT_thread


#class  Data_MQTT():
#    """Общий класс входящей информации"""
#    def __init__(self, topic, payload):
#        self.topic = str(topic)
#        self.payload = str(payload, 'UTF-8')


psycopg = threading.Timer(3, psycopg_test.try_thread)
mqtt = threading.Timer(1, MQTT_thread.start_one())


mqtt.start()
psycopg.start()









