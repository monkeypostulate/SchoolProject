from database.connect_to_database import ConnectToDataBase


sql_reset_table = """
CREATE SNAPSHOT TABLE 
school.selected_table_backup CLONE school.selected_table 
FOR SYSTEM_TIME AS OF TIMESTAMP(@TimeStampRestart);

DELETE 
school.student WHERE 1 = 1;

INSERT INTO school.selected_table
SELECT
*
FROM 
school.selected_table_backup WHERE 1 = 1;

DROP SNAPSHOT TABLE
school.selected_table_backup;
"""

class reset_database():
    def __init__(self):
        pass
    @staticmethod
    def reset_table(timestamp = '2022-09-06 15:15:56.649703 UTC',
               table = None):
        global sql_reset_table
        sql_reset_table = sql_reset_table.replace(
            'selected_table',
            table)
        
        parameters={'TimeStampRestart': "STRING"}
        values = [timestamp]
        connect_db=ConnectToDataBase()    

        result = connect_db.run_query(sql_reset_table,
                                       parameters,
                                       values)
        return True

    def recover_school_database(self,timestamp = '2022-09-06 15:15:56.649703 UTC'):
        list_tables = ['course', 'course2schedule','grades', 'schedule',
                       'student', 'student2course', 'student_grade']
        for table in list_tables:
            self.reset_table(timestamp = timestamp,
                       table = table)
        
        return True
    @staticmethod
    def reset_school_database():
        connect_db=ConnectToDataBase()    
        result = connect_db.run_query(sql_reset_table,
                                       parameters = None,
                                       values = None)
        
        return True
        
    
    


    
sql_start_database_from_zero = """

DROP TABLE school.course;
DROP TABLE school.course2schedule;
DROP TABLE school.grades;
DROP TABLE school.schedule;
DROP TABLE school.student;
DROP TABLE school.student2course;
DROP TABLE school.student_grade;



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


"""