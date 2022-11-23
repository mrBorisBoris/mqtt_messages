import json

def data_filter(data):
    data_dict = json.loads(data)
    modem_id = (data_dict['commandParams']['MeterParams']['SerialNumber'])
    ev_time = data_dict['eventsParams']['Events'][0]['Time']
    ev_code = data_dict['eventsParams']['Events'][0]['EventInfo']['EventCode']
    ev_type = data_dict['eventsParams']['Events'][0]['EventInfo']['EventType']
    ev_journal = data_dict['eventsParams']['Events'][0]['EventInfo']['JournalType']
    all_data = (modem_id, ev_time, ev_code, ev_type, ev_journal)
    return all_data
    # Функция при её вызове возвращает готовый кортеж для отправки в postgre
