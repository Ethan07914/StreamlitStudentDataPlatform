import pandas as pd

def IsMale(row):
    if row['Sex'] == 'M':
        row['IsMale'] = 1
    else:
        row['IsMale'] = 0
    return row

def HasRuralAddress(row):
    if row['AddressType'] == 'R':
        row['IsRuralAddress'] = 1
    else:
        row['IsRuralAddress'] = 0
    return row

def FamilySizeGreaterThanThree(row):
    if row['FamilySize'] == 'GT3':
        row['FamilySizeGreaterThanThree'] = 1
    else:
        row['FamilySizeGreaterThanThree'] = 0
    return row


def ParentsSeperated(row):
    if row['ParentLivingStatus'] == 'A':
        row['ParentsSeperated'] = 1
    else:
        row['ParentsSeperated'] = 0
    return row

def CommuteTimeGreaterThan(row):
    if row['Commute'] == '<15 minutes':
        row['CommuteTimeGreaterThan'] = 0
    elif row['Commute'] == '15-30 minutes':
        row['CommuteTimeGreaterThan'] = 15
    elif row['Commute'] == '30-60 minutes':
        row['CommuteTimeGreaterThan'] = 30
    else:
        row['CommuteTimeGreaterThan'] = 60
    return row

def ChoseSchoolFor(row):
    if row['ReasonForSchoolChoice'] == 'course':
        row['ChoseSchoolForCourse'], row['ChoseSchoolForReputation'], row['ChoseSchoolForProximity'] = 1, 0, 0
    elif row['ReasonForSchoolChoice'] == 'reputation':
        row['ChoseSchoolForCourse'], row['ChoseSchoolForReputation'], row['ChoseSchoolForProximity'] = 0, 1, 0
    elif row['ReasonForSchoolChoice'] == 'home':
        row['ChoseSchoolForCourse'], row['ChoseSchoolForReputation'], row['ChoseSchoolForHome'] = 0, 0, 1
    else:
        row['ChoseSchoolForCourse'], row['ChoseSchoolForReputation'], row['ChoseSchoolForHome'] = 0, 0, 0
    return row

def StudyHoursGreaterThan(row):
    if row['TimeSpentStudying'] == '<2 hours':
        row['StudyHoursGreaterThan'] = 0
    elif row['TimeSpentStudying'] == '2-5 hours':
        row['StudyHoursGreaterThan'] = 2
    elif row['TimeSpentStudying'] == '5-10 hours':
        row['StudyHoursGreaterThan'] = 5
    else:
        row['StudyHoursGreaterThan'] = 10
    return row

def ConvertBoolToInt(row):
    BoolCols =  ['EducationalSupport', 'ParentalSupport', 'ReceivesTutoring', 'ExtraCurricular',
                 'AttendedNursery', 'PlansOnHigherEducation', 'HasInternet', 'InRelationship']
    for col in BoolCols:
        if row[col] == 'yes':
            row[col] = 1
        else:
            row[col] = 0
    return row




