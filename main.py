import threading
import MQTT_start
import paho.mqtt.client as mqtt
import postgre
import postgre_get_data


def start_one():
    MQTT_starter = MQTT_start.MQTT(client=mqtt.Client(client_id="client1",
                                                      clean_session=True,
                                                      userdata=None,
                                                      protocol=mqtt.MQTTv311,
                                                      transport="tcp"))
    MQTT_starter.MQTT_start()

thread_1 = threading.Timer(15, start_one)
thread_1.start()

thread_2 = threading.Thread(target=postgre_get_data.connect_now(), args=())
thread_2.start()










