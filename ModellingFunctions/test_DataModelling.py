from DataModelling import *
import pandas as pd

def TestIsMale():
    # row = pd.DataFrame({'Sex': 'M'}, index=[0])
    row = pd.DataFrame({'Sex': 'F'}, index=[0])
    #If Sex is female then the IsMale column should be set to zero
    assert row.apply(IsMale, axis=1).iloc[0].IsMale == 0

# TestIsMale()

def TestRuralAddress():
    #row = pd.DataFrame({'AddressType': 'R'}, index=[0])
    row = pd.DataFrame({'AddressType': 'U'}, index=[0])
    #If address type is U for Urban IsRuralAddress column should be set to 0 for False
    assert row.apply(HasRuralAddress, axis=1).iloc[0].IsRuralAddress == 0

# TestRuralAddress()

def TestFamilySize():
    # row = pd.DataFrame({'FamilySize': 'GT3'}, index=[0])
    row = pd.DataFrame({'FamilySize': 'LT3'}, index=[0])
    #If Family size is less than 3 FamilySizeGreaterThan3 column should be set to 0
    assert row.apply(FamilySizeGreaterThanThree, axis=1).iloc[0].FamilySizeGreaterThanThree == 0

# TestFamilySize()

def TestParentsSeperated():
    # row = pd.DataFrame({'ParentLivingStatus': 'A'}, index=[0])
    row = pd.DataFrame({'ParentLivingStatus': 'T'}, index=[0])
    #If ParentsLivingStatus doesn't equal A Parents Seperated should be set to 0
    assert row.apply(ParentsSeperated, axis=1).iloc[0].ParentsSeperated == 0

# TestParentsSeperated()

def TestCommuteTime():
    tests = [['<15 minutes', 0], ['15-30 minutes', 15], ['30-60 minutes', 30], ['>1 hour', 60]]
    for test in tests:
        row = pd.DataFrame({'Commute': test[0]}, index=[0])
        assert row.apply(CommuteTimeGreaterThan, axis=1).iloc[0].CommuteTimeGreaterThan == test[1]

# TestCommuteTime()

def TestChoseSchoolFor():
    tests = [['course', 1, 0, 0], ['reputation', 0, 1, 0], ['home', 0, 0, 1], ['other', 0, 0, 0]]
    for test in tests:
        row = pd.DataFrame({'ReasonForSchoolChoice': test[0]}, index=[0])
        #Convert result to dictionary to allow for comparison
        assert row.apply(ChoseSchoolFor, axis=1).iloc[0].to_dict() == {'ReasonForSchoolChoice': test[0],
                                                                       'ChoseSchoolForCourse': test[1],
                                                                       'ChoseSchoolForReputation': test[2],
                                                                       'ChoseSchoolForProximity': test[3]}

# TestChoseSchoolFor()

def TestStudyHours():
    tests = [['<2 hours', 0], ['2-5 hours', 2], ['5-10 hours', 5], ['>10 hours', 10]]
    for test in tests:
        row = pd.DataFrame({'TimeSpentStudying': test[0]}, index=[0])
        assert row.apply(StudyHoursGreaterThan, axis=1).iloc[0]['StudyHoursGreaterThan'] == test[1]

# TestStudyHours()

def TestConvertBoolToInt():
    test_dict = {}
    cols = ['EducationalSupport', 'ParentalSupport', 'ReceivesTutoring', 'ExtraCurricular',
                 'AttendedNursery', 'PlansOnHigherEducation', 'HasInternet', 'InRelationship'] #All the same cols as used in the function being tested
    for col in cols:
        # test_dict[col] = 'yes'
        test_dict[col] = 'no' #Set the value of each key to no
    row = pd.DataFrame(test_dict, index=[0])
    # assert list(row.apply(ConvertBoolToInt, axis=1).iloc[0].to_dict().values()) == [1,1,1,1,1,1,1,1]
    assert list(row.apply(ConvertBoolToInt, axis=1).iloc[0].to_dict().values()) == [0,0,0,0,0,0,0,0] #If working 0 should be stored in all columns
    #Converts the dataframe to a dictionary then only selects the values not keys as a list

# TestConvertBoolToInt()

def TestEquivalent():
    row = pd.DataFrame({'ExamThreeGrade':15}, index=[0])
    # assert row.apply(FindEquivalent, axis=1, value=12).iloc[0].Equivalent == 'No'
    assert row.apply(FindEquivalent, axis=1, value=15).iloc[0].Equivalent == 'Yes'


# TestEquivalent()
