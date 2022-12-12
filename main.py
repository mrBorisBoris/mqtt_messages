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

#postgre_get_data.check_message_to_mqtt()
thread_1 = threading.Thread(target=start_one(), args=())
thread_1.start()

thread_2 = threading.Thread(target=postgre_get_data.check_message_to_mqtt(), args=())
thread_2.start()
# psycopg = threading.Timer(3, psycopg_test.try_thread)
# psycopg.start()









