import threading
import MQTT_start
import paho.mqtt.client as mqtt
import postgre

def start_one():
    MQTT_starter = MQTT_start.MQTT(client=mqtt.Client(client_id="client1",
                                                      clean_session=True,
                                                      userdata=None,
                                                      protocol=mqtt.MQTTv311,
                                                      transport="tcp"))
    MQTT_starter.MQTT_start()



thread_1 = threading.Thread(target=start_one(), args=())
#psycopg = threading.Timer(3, psycopg_test.try_thread)
#psycopg.start()









