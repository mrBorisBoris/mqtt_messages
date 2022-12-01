import paho.mqtt.client as mqtt
import MQTT_start

import threading






#class  Data_MQTT():
#    """Общий класс входящей информации"""
#    def __init__(self, topic, payload):
#        self.topic = str(topic)
#        self.payload = str(payload, 'UTF-8')

def start_one():
    MQTT_starter = MQTT_start.MQTT(client=mqtt.Client(client_id="client1",
                                                      clean_session=True,
                                                      userdata=None,
                                                      protocol=mqtt.MQTTv311,
                                                      transport="tcp"))
    MQTT_starter.MQTT_start()


t = threading.Thread(target=start_one(), args=())
t.start()







