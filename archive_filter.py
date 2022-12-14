import json
import datetime
from postgre_class import db

def archive_filter(topic, data):
    topic_data = topic
    all_data = data
    print(type(data))
    archive = json.loads(data)
    archive_number = archive['archiveNumber']
    if archive_number == 2:
        modem_id = archive['commandParams']['MeterParams']['SerialNumber']

        act = archive['archiveValues'][0]['Values']
        act_1 = archive['archiveValues'][0]['Values'][1]
        act_2 = archive['archiveValues'][0]['Values'][2]
        react = archive['archiveValues'][1]['Values']
        act_minus = archive['archiveValues'][2]['Values']
        react_minus = archive['archiveValues'][3]['Values']
        dev_time = archive['archiveValues'][0]['Time']
        datetime_time = datetime.datetime.strptime(dev_time, '%Y-%m-%dT%H:%M:%S')
        all_data = (modem_id, act, act_1, act_2, react, act_minus, react_minus, datetime_time, all_data)
        return all_data
    else:
        topic_to_insert = topic_data
        record_to_insert = (str(topic_to_insert), (str(data)))
        flag = False
        db.insert_into(record_to_insert, flag)
        return None
