from database.connect_to_database import ConnectToDataBase, JobConfig
import datetime




check_student = """
SELECT
COUNT(*) AS FlagStudent
FROM
school.student2course
WHERE
StudentId = @StudentId
AND CourseId = @CourseId
"""



sql_schedules_do_not_overlap = """
SELECT
MAX(CASE WHEN 
(
(StartHour <= @StartHour AND @StartHour <= ENDHour) 
OR  (StartHour <= @EndHour AND @EndHour <= ENDHour)
OR  (StartHour >= @StartHour AND @EndHour >= ENDHour)
)
AND 
(
(co.StartDate <= @StartDate  AND  @StartDate <= co.EndDate)
OR
(co.StartDate <= @EndDate  AND  @EndDate <= co.EndDate)
OR
(co.StartDate >= @StartDate  AND  @EndDate >= co.EndDate)
)
 THEN 1 ELSE 0 END)
AS FlagScheduleOverlap
FROM 
school.course AS co
INNER JOIN
school.course2schedule AS cs
ON
co.CourseId = cs.CourseId
INNER JOIN
school.schedule AS sc
ON 
cs.ScheduleId = sc.ScheduleId
INNER JOIN 
school.student2course AS stco
ON 
co.CourseId = stco.CourseId
WHERE
stco.StudentId = @StudentId
"""


sql_exist = """
WITH
course_exist
AS
(
SELECT
CASE WHEN COUNT(*)>0  THEN 1 ELSE 0 END AS FlagExist 
FROM 
school.course
WHERE 
CourseId = @CourseId
)
,
student_exist
AS
(
SELECT
CASE WHEN COUNT(*)>0  THEN 1 ELSE 0 END AS FlagExist 
FROM 
school.student
WHERE 
StudentId = @StudentId
)

SELECT
MAX(CASE WHEN s.FlagExist IS NULL THEN 0 ELSE s.FlagExist END*
CASE WHEN C.FlagExist IS NULL THEN 0 ELSE C.FlagExist END) AS FlagExist
FROM 
course_exist AS c
FULL OUTER JOIN 
student_exist AS s
ON
c.FlagExist  = s.FlagExist
"""

##ValidateStudentGrade
class ValidateStudentCourseInfo():
    def __init__(self):
        pass
    @staticmethod
    def valid_grade(grade):
        if grade in ['A','B','C','D','F']:
            return True
        else:
            raise ValueError('Invalid Grade')
    @staticmethod
    def valid_student_in_course(course_id = None,
                      student_id = None):
        parameters={'CourseId': "INT64",'StudentId':"INT64"}
        values = [course_id, student_id]
        connect_db=ConnectToDataBase()    
        results = connect_db.run_query(check_student,
                                       parameters,
                                      values)
        if results.to_dataframe().loc[0,'FlagStudent']>0:
            True
        else:
            raise ValueError('Student not in course')

    @staticmethod
    def check_student_course_exist(student_id, course_id):
        parameters={'CourseId': "INT64",'StudentId':"INT64"}
        values = [course_id, student_id]
        connect_db=ConnectToDataBase()    
        results = connect_db.run_query(sql_exist,
                                       parameters,
                                      values)
        if results.to_dataframe().loc[0,'FlagExist']>0:
            True
        else:
            raise ValueError('Student or Course do not exist')




class ValidateStudentInformation():
    def __init__(self):
        pass
    @staticmethod
    def check_student_names(first_name, family_name):
        if len(first_name) == 0 or len(family_name) == 0:
            raise ValueError('Name too short')
        return True
    @staticmethod
    def check_credit_capacity(credit_capacity):
        if not isinstance(credit_capacity,int):
            raise ValueError('Credit Capacity must be an integer')
        if not credit_capacity in range(1,20):
            raise ValueError('Credit Capacity out of range')
        return True
    

        





class ValidateCourseInformation():
    def __init__(self):
        pass
    @staticmethod
    def check_credit(credit):
        if not isinstance(credit,int):
            raise ValueError('Credit must be an integer')
        if not credit in range(1,11):
            raise ValueError('Credit out of range')
        return True
 
    @staticmethod
    def check_capacity(capacity):
        if not isinstance(capacity,int):
            raise ValueError('Capacity must be an integer')
        if not capacity in range(1,20):
            raise ValueError('Capacity out of range')
        return True

    @staticmethod
    def validate_date(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return True
            
    @staticmethod
    def check_start_date_end_date(start_date, end_date):
        if start_date>end_date:
            raise ValueError("Start Date Cannot be greater than end date")
        else:
            True






class ValidateSchedule():
    def __init__(self):
        pass
    @staticmethod
    def non_overlap_schedule(start_date = None,
                            end_date = None,
                            start_hour =None,
                            end_hour = None,
                            student_id = None):
        connect_db = ConnectToDataBase()
    
        parameters = {'StartDate': 'DATE', 'EndDate': 'DATE',
                      'StartHour': 'FLOAT64', 'EndHour': 'FLOAT64',
                     "StudentId": "INT64"}
        values = [start_date, end_date,
                  start_hour, end_hour,
                  student_id]
        
        results = connect_db.run_query(sql_schedules_do_not_overlap,
                             parameters,
                             values).to_dataframe()
        if not results['FlagScheduleOverlap'].loc[0]==1:
            return True
        else:
            raise ValueError("Conflict schedules")

            
