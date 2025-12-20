import sqlite3 as sql

con = sql.connect('studentperformance.db') #Establish connection to database
curs = con.cursor() #Create a cursor to interact with database

#Not using autoincrement on StudentID as will be generating that using pandas
curs.execute('''
CREATE TABLE IF NOT EXISTS Student
(StudentID INTEGER PRIMARY KEY, 
SchoolID INTEGER, 
Sex TEXT,
Age INTEGER,
AddressType TEXT,
FamilySize INTEGER,
GuardianOneID INTEGER,
GuardianTwoID INTEGER,
ParentLivingStatus TEXT,
Commute TEXT,
ReasonForSchoolChoice TEXT,
TimeSpentStudying TEXT,
FailureCount INTEGER,
EducationalSupport BOOLEAN,
ParentalSupport BOOLEAN,
ReceivesTutoring BOOLEAN,
ExtraCurricular BOOLEAN,
AttendedNursery BOOLEAN,
PlansOnHigherEducation BOOLEAN,
HasInternet BOOLEAN,
InRelationship BOOLEAN,
FamilyRelationshipRating INTEGER,
BusynessScale INTEGER,
SocialScore INTEGER,
WeekdayAlcoholConsumption INTEGER,
WeekendAlcoholConsumption INTEGER,
HealthScore INTEGER,
AbsenceCount INTEGER)
''')

curs.execute('''
CREATE TABLE IF NOT EXISTS School
(SchoolID INTEGER PRIMARY KEY AUTOINCREMENT,
 Country TEXT,
 Name TEXT)
 ''')

curs.execute('''
CREATE TABLE IF NOT EXISTS Exam
(ExamID INTEGER PRIMARY KEY AUTOINCREMENT,
Code TEXT,
Description TEXT)''')

curs.execute('''
CREATE TABLE IF NOT EXISTS ExamEntry
(ExamEntryID INTEGER PRIMARY KEY AUTOINCREMENT,
ExamID INTEGER,
StudentID INTEGER,
Grade INTEGER
)''')

curs.execute('''
CREATE TABLE IF NOT EXISTS EducationLevel
(EducationLevelID INTEGER PRIMARY KEY AUTOINCREMENT ,
Description TEXT)''')

#Not autoincrementing GuardianID as will create that using Pandas
curs.execute('''
CREATE TABLE IF NOT EXISTS Guardian
(GuardianID INTEGER PRIMARY KEY,
RelationshipToStudent TEXT,
EducationLevelID INTEGER, 
OccupationID INTEGER,
IsPrimary BOOLEAN)
''')

curs.execute('''
CREATE TABLE IF NOT EXISTS Occupation
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
Description TEXT)''')


# curs.execute('''
# UPDATE EducationLevel
# SET EducationLevelID = EducationLevelID - 1''')

con.commit()




