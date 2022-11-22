import configparser
import os


class Other:
    def __init__(self, ini_path, ini_name):
        self.ini_path = ini_path
        self.ini_name = ini_name


config = configparser.ConfigParser()

# mqtt

config['MQTT'] = {}
config['MQTT']['host'] = '93.188.43.181'
config['MQTT']['port'] = str(8883)
config['MQTT']['user'] = 'client1'
config['MQTT']['password'] = 'aineekeechohdoo7haecah3r'

# postgre

config['POSTGRE'] = {}
config['POSTGRE']['user'] = 'psqlar'
config['POSTGRE']['password'] = 'Hgft667rD454w4e'
config['POSTGRE']['port'] = str(5432)
config['POSTGRE']['database'] = "postgres"
config['POSTGRE']['host'] = "172.20.19.48"


# other

config['other'] = {}
config['other']['ini_path'] = os.path.abspath('mqtt_messages/config.ini')
config['other']['ini_name'] = 'config.ini'
# print(config['93.188.43.181']['user'])
# print(config['other']['ini_path'])
with open('config.ini', 'w') as configfile:
    config.write(configfile)
# print(config.sections())
# print(os.path.abspath('mqtt_messages/config.ini'))

# file_name = os.path.abspath('mqtt_messages/config.ini')
other = Other(os.path.abspath('mqtt_messages/config.ini'), 'config.ini')

# print(other.ini_name)
# print(other.ini_path)






