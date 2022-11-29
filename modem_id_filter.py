
def filter_modems(data):
    string = data
    modem = []
    for word in string.split('/'):
        try:
            modem.append(int(word))
        except ValueError:
            pass

    #print(modem)

    if modem[0] in range(47208000, 47208099):
        #print('ok')
        return True
    elif modem[0] in range(47236509, 47236518):
        #print('ok')
        return True
    else:
        #print('not ok')
        return False
