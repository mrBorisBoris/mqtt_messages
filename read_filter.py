import re
from postgre_get_data import setsend
from postgre_get_data import setanswer


def filter_topic(topic_data, payload_data):
    if 'Answer' in topic_data:
        new_answer_topic = re.sub(r'\b/Result\b', '', topic_data, flags=re.IGNORECASE)
        print(new_answer_topic)
        setanswer(str(new_answer_topic), payload_data)

    if 'ToMeter' in topic_data:
        if 'Result' in topic_data:
            new_topic = re.sub(r'\b/Result\b', '', topic_data, flags=re.IGNORECASE)
            print(new_topic)
            setsend(str(new_topic), payload_data)

        else:
            pass
