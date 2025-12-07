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












