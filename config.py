import configparser
import os


class Other:
    def __init__(self, ini_path, ini_name):
        self.ini_path = os.path.abspath('mqtt_messages/config.ini')
        self.ini_name = 'config.ini'


config = configparser.ConfigParser()

# mqtt

config['93.188.43.181'] = {}
config['93.188.43.181']['port'] = str(8883)
config['93.188.43.181']['user'] = 'client1'
config['93.188.43.181']['password'] = 'aineekeechohdoo7haecah3r'

# postgre

config['172.20.19.48'] = {}
config['172.20.19.48']['user'] = 'psqlar'
config['172.20.19.48']['password'] = 'Hgft667rD454w4e'

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






