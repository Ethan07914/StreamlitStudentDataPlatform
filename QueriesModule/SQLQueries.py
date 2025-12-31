BaseQuery = \
'''
SELECT s.StudentID, sch.SchoolID, sch.Name AS SchoolName, Sex, Age, AddressType, FamilySize, ParentLivingStatus, Commute, ReasonForSchoolChoice, TimeSpentStudying, FailureCount, EducationalSupport, ParentalSupport
, ReceivesTutoring, ExtraCurricular, AttendedNursery, PlansOnHigherEducation, HasInternet, InRelationship, FamilyRelationshipRating, BusynessScale, SocialScore, WeekdayAlcoholConsumption, WeekendAlcoholConsumption
, HealthScore, AbsenceCount, GuardianOneId, MothersOccupationID, MothersOccupation, MothersEducationLevel, GuardianTwoID, FathersOccupationID, FathersOccupation, FathersEducationLevel, 
IsFatherPrimary, IsMotherPrimary,
CASE 
    WHEN IsFatherPrimary = 1 THEN 'Father'
    ELSE 'Mother'
END AS PrimaryGuardian,
E1.Grade AS ExamOneGrade, E2.Grade AS ExamTwoGrade, E3.Grade AS ExamThreeGrade
    FROM Student AS s
    INNER JOIN 
    (SELECT g.GuardianID, g.OccupationID As MothersOccupationID, o.description as MothersOccupation,
     g.EducationLevelID AS MothersEducationLevel, g.IsPrimary AS IsMotherPrimary
        FROM Guardian AS g
        INNER JOIN EducationLevel AS el
        ON g.EducationLevelID = el.EducationLevelID
        INNER JOIN Occupation AS o
        ON g.OccupationID = o.ID
            WHERE RelationshipToStudent = "Mother")
    AS m on s.GuardianOneID = m.GuardianID
    INNER JOIN 
    (SELECT g.GuardianID, g.OccupationID AS FathersOccupationID, o.Description as FathersOccupation,
     g.EducationLevelID AS FathersEducationLevel, g.IsPrimary AS IsFatherPrimary
        FROM Guardian AS g
        INNER JOIN EducationLevel AS el
        ON g.EducationLevelID = el.EducationLevelID
        INNER JOIN Occupation AS o
        ON g.OccupationID = o.ID
            WHERE RelationshipToStudent = "Father")
    AS f on s.GuardianTwoID = f.GuardianID
    INNER JOIN School AS sch ON s.SchoolID = sch.SchoolID
    INNER JOIN 
    (SELECT StudentID, Grade
        FROM ExamEntry AS ee
        INNER JOIN Exam AS e
        ON ee.ExamID = e.ExamID
            WHERE e.Code = "G1")
    AS E1 ON s.StudentID = E1.StudentID
    INNER JOIN 
    (SELECT StudentID, Grade
        FROM ExamEntry AS ee
        INNER JOIN Exam AS e
        ON ee.ExamID = e.ExamID
            WHERE e.Code = "G2")
    AS E2 ON s.StudentID = E2.StudentID
    INNER JOIN 
    (SELECT StudentID, Grade
        FROM ExamEntry AS ee
        INNER JOIN Exam AS e
        ON ee.ExamID = e.ExamID
            WHERE e.Code = "G3")
    AS E3 ON s.StudentID = E3.StudentID'''


