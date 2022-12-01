import paho.mqtt.client as mqtt
import MQTT_start
import postgre_get_data



#class  Data_MQTT():
#    """Общий класс входящей информации"""
#    def __init__(self, topic, payload):
#        self.topic = str(topic)
#        self.payload = str(payload, 'UTF-8')


MQTT_starter = MQTT_start.MQTT(client=mqtt.Client(client_id="client1",
                                  clean_session=True,
                                  userdata=None,
                                  protocol=mqtt.MQTTv311,
                                  transport="tcp"))
postgre_get_data.check_message_to_mqtt()
MQTT_starter.MQTT_start()



