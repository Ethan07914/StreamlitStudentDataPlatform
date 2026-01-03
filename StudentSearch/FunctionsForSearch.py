def GetFilterValues(Entered, Options):
    Values = []
    if Entered in Options[1:3]:
        Values.append([Entered])
    else:
        Values.append(Options[1:3])
    return Values

def InequalitiesCalculator(frame, col, inequality='≥ Greater than or equal to', value=0):
    value = int(value)
    if inequality == '< Less than':
        return frame[col] < value
    elif inequality == '≤ Less than or equal to':
        return frame[col] <= value
    elif inequality == '> Greater than':
        return frame[col] > value
    elif inequality == '≥ Greater than or equal to':
        return frame[col] >= value
    elif inequality == '= Equal to':
        return frame[col] == value
    else:
        return frame[col] != value