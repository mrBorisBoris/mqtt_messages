import json
import datetime


def data_filter(data):
    data_dict = json.loads(data)
    modem_id = (data_dict['commandParams']['MeterParams']['SerialNumber'])
    ev_time = data_dict['eventsParams']['Events'][0]['Time']
    ev_time_datetime_format = datetime.datetime.strptime(ev_time, '%Y-%m-%dT%H:%M:%S')
    ev_code = data_dict['eventsParams']['Events'][0]['EventInfo']['EventCode']
    ev_type = data_dict['eventsParams']['Events'][0]['EventInfo']['EventType']
    ev_journal = data_dict['eventsParams']['Events'][0]['EventInfo']['JournalType']
    all_data = (str(modem_id), ev_time_datetime_format, int(ev_code), int(ev_type), int(ev_journal))
    return all_data
    # Функция при её вызове возвращает готовый кортеж для отправки в postgre
