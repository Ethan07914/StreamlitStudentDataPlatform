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

Exams = ('G1', 'G2', 'G3') #Tuple of exam names
# for exam in Exams:
#     curs.execute('''
#     INSERT INTO Exam
#     (Name)
#     VALUES (?)''',
#                  (exam,))
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

print(Data[['StudentID', 'Medu', 'Mjob', 'Fedu', 'Fjob']])






