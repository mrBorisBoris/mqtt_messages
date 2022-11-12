import configparser
import os


class Other:
    def __init__(self, ini_path, ini_name):
        self.ini_path = os.path.abspath('mqtt_messages/config.ini')
        self.ini_name = 'config.ini'


config = configparser.ConfigParser()
config['93.188.43.181'] = {}
config['93.188.43.181']['port'] = str(8883)
config['93.188.43.181']['user'] = 'client1'
config['93.188.43.181']['password'] = 'aineekeechohdoo7haecah3r'
print(config['93.188.43.181']['user'])
with open('config.ini', 'w') as configfile:
    config.write(configfile)
print(config.sections())
print(os.path.abspath('mqtt_messages/config.ini'))

file_name = os.path.abspath('mqtt_messages/config.ini')
other = Other(os.path.abspath('mqtt_messages/config.ini'), 'config.ini')
print(other.ini_name)
print(other.ini_path)






