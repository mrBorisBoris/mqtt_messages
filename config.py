import configparser

config = configparser.ConfigParser()
config['93.188.43.181'] = {}
config['93.188.43.181']['port'] = str(8883)
config['93.188.43.181']['user'] = 'client1'
config['93.188.43.181']['password'] = 'aineekeechohdoo7haecah3r'
print(config['93.188.43.181']['user'])
with open('example.ini', 'w') as configfile:
    config.write(configfile)
print(config.sections())
