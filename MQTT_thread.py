import MQTT_start
import paho.mqtt.client as mqtt

def start_one():
    MQTT_starter = MQTT_start.MQTT(client=mqtt.Client(client_id="client1",
                                                      clean_session=True,
                                                      userdata=None,
                                                      protocol=mqtt.MQTTv311,
                                                      transport="tcp"))
    MQTT_starter.MQTT_start()
