import json
import queue
import datetime
import logger_file

queue_to_insert = queue.Queue()


def many_days(topic, payload):

    try:
        topic_data = topic
        all_data = payload
        first_string_topic = str(topic)
        first_string_payload = str(payload)

        archive = json.loads(all_data)

        values = archive["archiveValues"]


        modem_id = int(archive["completeParams"]["MeterParams"]["SerialNumber"])
        command_id = int(archive["completeParams"]["CommandState"])
        if command_id == 3:

            data_values = []
            for i_data in values:
                data_values.append(i_data)

            date_dict = {}
            for i_date in data_values:
                if i_date['Time'] not in date_dict:
                    date_dict[i_date['Time']] = {}


            for value in data_values:
                if value['Time'] in date_dict:
                    date_dict[value['Time']][value['ValueType']] = value


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
                a2 = ',  (select id from jst)),'
                all_data = (modem_id, act, act_1, act_2, react, act_minus, react_minus, dev_time)
                all_data = str(all_data)
                all_data = all_data[:-1]
                all_data += '::timestamp'
                all_data += a2
                print('ALL PARSED DATA = ', all_data)
                queue_to_insert.put(all_data)

            data = queue_to_insert.queue
            print(len(data))
            data_beta = ''
            for i in range(len(data)):
                data_beta += data[i]
            print('DATA BETA = ', data_beta)
            data_beta = data_beta[:-1]
            print('DATA BETA = ', data_beta)
            data_beta = data_beta.replace("[", "'{")
            data_beta = data_beta.replace("]", "}'")
            return first_string_topic, first_string_payload, data_beta

    except TypeError:
        logger_file.logging.error('TypeError', exc_info=True)
        pass



