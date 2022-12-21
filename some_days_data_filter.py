import json
import queue
import datetime

queue_to_insert = queue.Queue()


a = {
    "completeParams": {
        "CommandId": 2,
        "CommandState": 3,
        "MeterParams": {
            "MeterType": 11,
            "SerialNumber": "47208025"
        },
        "CommandHeader": {
            "DateTime": "2022-12-16T14:45:57",
            "Command": 3,
            "ErrorCode": 0
        }
    },
    "archiveNumber": 2,
    "archiveValues": [{
        "Time": "2022-12-08T00:00:00",
        "ValueType": 1,
        "Quality": 0,
        "Values": [1551002.0, 1257548.0, 293454.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-09T00:00:00",
        "ValueType": 1,
        "Quality": 0,
        "Values": [1556418.0, 1261422.0, 294996.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-10T00:00:00",
        "ValueType": 1,
        "Quality": 0,
        "Values": [1578660.0, 1282300.0, 296360.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-08T00:00:00",
        "ValueType": 2,
        "Quality": 0,
        "Values": [318.0, 318.0, 0.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-09T00:00:00",
        "ValueType": 2,
        "Quality": 0,
        "Values": [318.0, 318.0, 0.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-10T00:00:00",
        "ValueType": 2,
        "Quality": 0,
        "Values": [318.0, 318.0, 0.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-08T00:00:00",
        "ValueType": 25,
        "Quality": 0,
        "Values": [94408.0, 82496.0, 11912.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-09T00:00:00",
        "ValueType": 25,
        "Quality": 0,
        "Values": [94992.0, 82884.0, 12108.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-10T00:00:00",
        "ValueType": 25,
        "Quality": 0,
        "Values": [95908.0, 83626.0, 12282.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-08T00:00:00",
        "ValueType": 26,
        "Quality": 0,
        "Values": [206728.0, 143384.0, 63344.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-09T00:00:00",
        "ValueType": 26,
        "Quality": 0,
        "Values": [208474.0, 144520.0, 63954.0, 0.0, 0.0]
    }, {
        "Time": "2022-12-10T00:00:00",
        "ValueType": 26,
        "Quality": 0,
        "Values": [211184.0, 146626.0, 64558.0, 0.0, 0.0]
    }]
}


b = json.dumps(a)
print(type(b))
archive = json.loads(b)
values = archive["archiveValues"]
print(len(values))
modem_id = a["completeParams"]["MeterParams"]["SerialNumber"]
data_values = []
for i_data in values:
    # print(i_data)
    data_values.append(i_data)

date_dict = {}
for i_date in data_values:
    if i_date['Time'] not in date_dict:
        date_dict[i_date['Time']] = {}

# print(date_dict)

for value in data_values:
    if value['Time'] in date_dict:
        date_dict[value['Time']][value['ValueType']] = value

# print(date_dict)

for i_key, i_value in date_dict.items():
    print(i_key)
    print(i_value)
    print('MODEM_ID = ', modem_id)
    print('ACT = ', i_value[1]['Values'])
    act = i_value[1]['Values']
    print('ACT1 = ', i_value[1]['Values'][1])
    act_1 = i_value[1]['Values'][1]
    print('ACT2 = ', i_value[1]['Values'][2])
    act_2 = i_value[1]['Values'][2]
    print('REACT = ', i_value[2]['Values'])
    react = i_value[2]['Values']
    print('ACT_MINUS = ', i_value[25]['Values'])
    act_minus = i_value[25]['Values']
    print('REACT_MINUS =', i_value[26]['Values'])
    react_minus = i_value[26]['Values']
    dev_time = i_value[1]['Time']
    datetime_time = datetime.datetime.strptime(dev_time, '%Y-%m-%dT%H:%M:%S')
    print('DEVTIME = ', datetime_time)
    original_data = archive
    print('DEVDATA = ', archive)
    all_data = (modem_id, act, act_1, act_2, react, act_minus, react_minus, datetime_time, archive)
    print('ALL PARSED DATA = ', all_data)
    queue_to_insert.put(all_data)



print(queue_to_insert.get())