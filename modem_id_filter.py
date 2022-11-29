def filter_modems(data):
    string = data
    modem = []
    for word in string.split('/'):
        try:
            modem.append(int(word))
        except ValueError:
            pass

    try:
        if modem[0] in range(47208000, 47208099):
            return True
        elif modem[0] in range(47236509, 47236518):
            return True
        else:
            return False
    except IndexError:
        return False
