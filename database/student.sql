CREATE OR REPLACE TABLE
school.student
(StudentId INT64,
FirstName STRING,
FamilyName STRING,
CreditCapacity FLOAT64,
Status FLOAT64,
DateStudentCreated  DATE
)
PARTITION BY
DateStudentCreated
