

CREATE OR REPLACE TABLE 
school.course
(
  CourseId INT,
  CourseName STRING,
  StartDate Date,
  EndDate Date,
  Credit FLOAT64,
  Capacity FLOAT64,
  InsertionDate TIMESTAMP
);

CREATE OR REPLACE TABLE
school.course2schedule
(CourseId INT64,
ScheduleId INT64
) ;


CREATE OR REPLACE TABLE 
school.grades(
  Grade STRING,
  GradeNumeric FLOAT64);


 CREATE OR REPLACE TABLE
school.schedule
(ScheduleId INT64,
 StartHour FLOAT64, 
 ENDHour FLOAT64
);


CREATE OR REPLACE TABLE
school.student
(StudentId INT64,
FirstName STRING,
FamilyName STRING,
CreditCapacity FLOAT64,
Status FLOAT64,
DateStudentCreated  date
)
PARTITION BY
DateStudentCreated;


CREATE OR REPLACE TABLE
school.student2course
(studentId INT,
CourseId INT
);


CREATE OR REPLACE TABLE 
school.student_grade(
  StudentId INT,
  CourseId int,
  Grade STRING
);
