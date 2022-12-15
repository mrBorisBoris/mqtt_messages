
from postgre_get_data import setsend


def filter_topic(topic_data, payload_data):
    if 'ToMeter' in topic_data:
        if 'Result' in topic_data:
            print(topic_data[:43])
            new_topic = topic_data[:43]
            setsend(str(new_topic), payload_data)

        else:
            pass
