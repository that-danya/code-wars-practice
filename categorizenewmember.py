def openOrSenior(data):
    placement = []

    for age, handic in data:
        if age >= 55 and handic >= 7:
            placement.append('Senior')
        else:
            placement.append('Open')
    return placement
