import json
import datetime

a = {'archiveNumber': 1, 'archiveValues': [{'Time': '2022-09-01T00:00:00', 'Values': [5536, 3820, 1716, 0, 0], 'Quality': 0, 'ValueType': 1}, {'Time': '2022-09-01T00:00:00', 'Values': [0, 0, 0, 0, 0], 'Quality': 0, 'ValueType': 2}, {'Time': '2022-09-01T00:00:00', 'Values': [650, 594, 56, 0, 0], 'Quality': 0, 'ValueType': 25}, {'Time': '2022-09-01T00:00:00', 'Values': [122, 108, 14, 0, 0], 'Quality': 0, 'ValueType': 26}], 'completeParams': {'CommandId': 1, 'MeterParams': {'MeterType': 11, 'SerialNumber': '47208075'}, 'CommandState': 3, 'CommandHeader': {'Command': 3, 'DateTime': '2022-11-27T20:52:41', 'ErrorCode': 0}}}


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
