from InsertToDB import *
import pandas as pd

def TestIsMotherPrimary():
    # row = pd.DataFrame({'guardian': 'mother'}, index=[0])
    row = pd.DataFrame({'guardian': 'father'}, index=[0])
    assert row.apply(IsMotherPrimary, axis=1).iloc[0].IsPrimary == False #If the value of guardian is father the IsMotherPrimary column should be set to false for that row

# TestIsMotherPrimary()


def TestIsFatherPrimary():
    row = pd.DataFrame({'guardian': 'mother'}, index=[0])
    # row = pd.DataFrame({'guardian': 'father'}, index=[0])
    assert row.apply(IsFatherPrimary, axis=1).iloc[0].IsPrimary == False

# TestIsFatherPrimary()

def TestOccupationID():
    tests = [['at_home', 1], ['health', 2], ['other', 3], ['services', 4], ['teacher', 5]] #list of all possible inputs and outputs
    for test in tests: #Iterate through all tests
        row = pd.DataFrame({'PlaceHolder1': None, 'PlaceHolder2': None, 'occupation': test[0]}, index=[0]) #Functions requires row to have three columns so placeholders are required in this instance
        assert row.apply(GetOccupationID, axis=1).iloc[0].OccupationID == test[1] #Plugging the input value into the function should result in the specified output contained within the list

# TestOccupationID()

def TestSchoolID():
    # row = pd.DataFrame({'school': 'GP'}, index=[0])
    row = pd.DataFrame({'school': 'MS'}, index=[0])
    # assert row.apply(GetSchoolID, axis=1).iloc[0].SchoolID == 1
    assert row.apply(GetSchoolID, axis=1).iloc[0].SchoolID == 2

# TestSchoolID()

def TestTravelTime():
    tests = [[1, '<15 minutes'], [2, '15-30 minutes'], [3, '30-60 minutes'], [4, '>1 hour']]
    for test in tests:
        row = pd.DataFrame({'traveltime': test[0]}, index=[0])
        assert row.apply(GetTravelTime, axis=1).iloc[0].traveltime == test[1]

# TestTravelTime()

def TestStudyTime():
    tests = [[1, '<2 hours'], [2, '2-5 hours'], [3, '5-10 hours'], [4, '>10 hours']]
    for test in tests:
        row = pd.DataFrame({'studytime': test[0]}, index=[0])
        assert row.apply(GetStudyTime, axis=1).iloc[0].studytime == test[1]

# TestStudyTime()