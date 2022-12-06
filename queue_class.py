import archive_filter
import filter
import postgre

class Queue_1():
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def get_data(self):
        return self.queue.pop(0)

    def is_not_empty(self):
        if len(self.queue) != 0:
            return True
        else:
            return False

    def data_filter(self):
        all_data = self.queue.pop(0)
        topic = all_data[0]
        payload = (str(all_data[1], 'UTF-8'))
        # print(topic)
        # print(payload)
        if 'Event/Archive' in topic:
            filtered_data_archive = archive_filter.archive_filter(topic, payload)
            if filtered_data_archive is not None:
                print(filtered_data_archive)
                flag = 'ArchiveNumber2'
                postgre.postgre_code(filtered_data_archive, flag)
        if 'Events' in topic:
            filtered_data = filter.data_filter(payload)
            flag = 'Events'
            postgre.postgre_code(filtered_data, flag)
        else:
            record_to_insert = (str(topic), str(payload))
            flag = False
            postgre.postgre_code(record_to_insert, flag)





