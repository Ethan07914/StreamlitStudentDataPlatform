def GetFilterValues(Entered, Options):
    Values = []
    if Entered in Options[1:3]:
        Values.append([Entered]) #If the user didn't select Either as the option return the actual value
    else:
        Values.append(Options[1:3]) #If the user did select Either return both the other two options
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


