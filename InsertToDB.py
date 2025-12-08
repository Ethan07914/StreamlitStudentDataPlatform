import pandas as pd
import sqlite3 as sql

con = sql.connect('studentperformance.db')
curs = con.cursor()

Data = pd.read_csv('studentperformance.csv') #Create DataFrame
Data = Data.reset_index().rename(columns={'index':'StudentID'}) #Give each row a unique StudentID

def GetUniqueValues(Series):
   return Series.unique() #Return unique values within a column/series

Schools = GetUniqueValues(Data['school'])
Country = 'Portugal'
# for school in Schools:
#     curs.execute('''
#     INSERT INTO School
#     (Country, Name)
#      VALUES (?, ?)''',
#                  (Country, school))
#     con.commit()

print(curs.execute('SELECT * FROM School').fetchall())

Exams = [{'Code': 'G1', 'Description': 'First Period Grade'},
         {'Code': 'G2', 'Description': 'Second Period Grade'},
         {'Code': 'G3', 'Description': 'Final Grade'}] #List of Exam dictionaries
# for exam in Exams:
#     curs.execute('''
#     INSERT INTO Exam
#     (Code, Description)
#     VALUES (?, ?)''',
#                  (exam["Code"], exam["Description"]))
#     con.commit()

print(curs.execute('SELECT * FROM Exam').fetchall())

EducationLevelDict = \
    {0: 'None'
    ,1: 'Primary (4th Grade)'
    ,2: '5th-9th Grade'
    ,3: 'Secondary'
    ,4: 'Higher'} #Describes what values in the csv file mean
# for Level in EducationLevelDict.values():
#     #Iterates through all values in dictionary
#     curs.execute('''
#     INSERT INTO EducationLevel
#     (Description)
#     VALUES (?)''',
#                  (Level,))
#     con.commit()

print(curs.execute('SELECT * FROM EducationLevel').fetchall())

def SetGuardianIDs(row, LengthOfDF):
    row['GuardianOneID'] = row['StudentID']
    row['GuardianTwoID'] = row['StudentID'] + LengthOfDF
    return row

Data = SetGuardianIDs(Data, len(Data))

def IsMotherPrimary(row):
    if row['guardian'] == 'mother':
        row['IsPrimary'] = True
    else:
        row['IsPrimary'] = False
    return row

def IsFatherPrimary(row):
    if row['guardian'] == 'father':
        row['IsPrimary'] = True
    else:
        row['IsPrimary'] = False
    return row

Mothers = Data[['GuardianOneID', 'Medu', 'Mjob', 'guardian']]
Mothers = Mothers.apply(IsMotherPrimary, axis='columns')
Mothers = Mothers.to_dict('records')
# for row in Mothers:
#     curs.execute('''
#     INSERT INTO Guardian
#     (GuardianID, RelationshipToStudent, EducationLevelID, Occupation, IsPrimary)
#     VALUES (?, ?, ?, ?, ?)''',
#                  (row['GuardianOneID'],
#                   'Mother',
#                   row['Medu'],
#                   row['Mjob'],
#                   row['IsPrimary']))
#     con.commit()

print(curs.execute('''
SELECT * FROM Guardian
    WHERE RelationshipToStudent = "Mother"''').fetchall())


Fathers = Data[['GuardianTwoID', 'Fedu', 'Fjob', 'guardian']]
Fathers = Fathers.apply(IsFatherPrimary, axis='columns')
Fathers = Fathers.to_dict('records')
# for row in Fathers:
#     curs.execute('''
#     INSERT INTO Guardian
#     (GuardianID, RelationshipToStudent, EducationLevelID, Occupation, IsPrimary)
#     VALUES (?, ?, ?, ?, ?)''',
#                  (row['GuardianTwoID'],
#                   'Father',
#                   row['Fedu'],
#                   row['Fjob'],
#                   row['IsPrimary']))
#     con.commit()

print(curs.execute('''
SELECT * FROM Guardian
    WHERE RelationshipToStudent = "Father"''').fetchall())


ExamsG1 = Data[['StudentID',  'G1']]
ExamsG1 = ExamsG1.to_dict('records')
# for Exam in ExamsG1:
#     curs.execute('''
#     INSERT INTO ExamEntry (ExamID, StudentID, Grade)
#     VALUES (?, ?, ?)''',
#                  (1, Exam['StudentID'], Exam['G1']))
#     con.commit()

print(curs.execute('''
SELECT * FROM ExamEntry
 WHERE ExamID = 1''').fetchall())

ExamsG2 = Data[['StudentID',  'G2']]
ExamsG2 = ExamsG2.to_dict('records')
# for Exam in ExamsG2:
#     curs.execute('''
#     INSERT INTO ExamEntry (ExamID, StudentID, Grade)
#     VALUES (?, ?, ?)''',
#                  (2, Exam['StudentID'], Exam['G2']))
#     con.commit()

print(curs.execute('''
SELECT * FROM ExamEntry
 WHERE ExamID = 2''').fetchall())

ExamsG3 = Data[['StudentID',  'G3']]
ExamsG3 = ExamsG3.to_dict('records')
# for Exam in ExamsG3:
#     curs.execute('''
#     INSERT INTO ExamEntry (ExamID, StudentID, Grade)
#     VALUES (?, ?, ?)''',
#                  (3, Exam['StudentID'], Exam['G3']))
#     con.commit()

print(curs.execute('''
SELECT * FROM ExamEntry
 WHERE ExamID = 3''').fetchall())

def GetSchoolID(row):
    if row['school'] == 'GP':
        row['SchoolID'] = 1
    elif row['school'] == 'MS':
        row['SchoolID'] = 2
    return row

def GetTravelTime(row):
    if row['traveltime'] == 1:
        row['traveltime'] = '<15 minutes'
    elif row['traveltime'] == 2:
        row['traveltime'] = '15-30 minutes'
    elif row['traveltime'] == 3:
        row['traveltime'] = '30-60 minutes'
    elif row['traveltime'] == 4:
        row['traveltime'] = '>1 hour'
    return row

def GetStudyTime(row):
    if row['studytime'] == 1:
        row['studytime'] = '<2 hours'
    elif row['studytime'] == 2:
        row['studytime'] = '2-5 hours'
    elif row['studytime'] == 3:
        row['studytime'] = '5-10 hours'
    elif row['studytime'] == 4:
        row['studytime'] = '>10 hours'
    return row

Data = Data.apply(GetSchoolID, axis='columns')
Data = Data.apply(GetTravelTime, axis='columns')
Data = Data.apply(GetStudyTime, axis='columns')

Students = Data[['StudentID', 'SchoolID', 'sex', 'age', 'address', 'famsize', 'GuardianOneID', 'GuardianTwoID',
                 'Pstatus', 'traveltime', 'reason', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid',
                 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout',
                 'Dalc', 'Walc', 'health', 'absences']]
Students = Students.to_dict('records')
# for student in Students:
#     curs.execute('''
#     INSERT INTO Student
#     (StudentID,
#     SchoolID,
#     Sex,
#     Age,
#     AddressType,
#     FamilySize,
#     GuardianOneID,
#     GuardianTwoID,
#     ParentLivingStatus,
#     Commute,
#     ReasonForSchoolChoice,
#     TimeSpentStudying,
#     FailureCount,
#     EducationalSupport,
#     ParentalSupport,
#     ReceivesTutoring,
#     ExtraCurricular,
#     AttendedNursery,
#     PlansOnHigherEducation,
#     HasInternet,
#     InRelationship,
#     FamilyRelationshipRating,
#     BusynessScale,
#     SocialScore,
#     WeekdayAlcoholConsumption,
#     WeekendAlcoholConsumption,
#     HealthScore,
#     AbsenceCount)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                  (student['StudentID'], student['SchoolID'], student['sex'], student['age'], student['address'], student['famsize'], student['GuardianOneID'], student['GuardianTwoID'],
#                  student['Pstatus'], student['traveltime'], student['reason'], student['studytime'], student['failures'], student['schoolsup'], student['famsup'], student['paid'],
#                  student['activities'], student['nursery'], student['higher'], student['internet'], student['romantic'], student['famrel'], student['freetime'], student['goout'],
#                  student['Dalc'], student['Walc'], student['health'], student['absences']))
#     con.commit()

print(curs.execute('''
SELECT * FROM Student LIMIT 10''').fetchall())











