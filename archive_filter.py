import json
import datetime
import postgre


def archive_filter(topic, data):
    topic_data = topic
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
        dev_data = json.dumps(archive)
        datetime_time = datetime.datetime.strptime(dev_time, '%Y-%m-%dT%H:%M:%S')
        all_data = (modem_id, act, act_1, act_2, react, act_minus, react_minus, datetime_time, dev_data)
        return all_data
    else:
        topic_to_insert = topic_data
        record_to_insert = (str(topic_to_insert), (str(data)))
        flag = False
        postgre.postgre_code(record_to_insert, flag)
        return None
