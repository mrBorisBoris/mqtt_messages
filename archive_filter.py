import json
import datetime


def archive_filter(data):
    a = json.loads(data)
    modem_id = a['completeParams']['MeterParams']['SerialNumber']
    act = a['archiveValues'][0]['Values']
    act_1 = a['archiveValues'][0]['Values'][1]
    print(act)
    print(act_1)
    act_2 = a['archiveValues'][0]['Values'][2]
    print(act_2)
    react = a['archiveValues'][1]['Values']
    print(react)
    act_minus = a['archiveValues'][2]['Values']
    print(act_minus)
    react_minus = a['archiveValues'][3]['Values']
    print(react_minus)
    dev_time = a['archiveValues'][0]['Time']
    print(dev_time)
    dev_time_datetime = datetime.datetime.strptime(dev_time, '%Y-%m-%dT%H:%M:%S')
    print(dev_time_datetime)
    all_data = (str(modem_id), act_1, act_2, react, act_minus, react_minus, dev_time_datetime)
    return all_data
