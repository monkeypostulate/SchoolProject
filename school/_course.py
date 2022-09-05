from school.event import Event
from school.connect_to_database import ConnectToDataBase
from datetime import datetime


sql_update_course="""
UPDATE 
school.course
SET
 CourseName = @CourseName
WHERE CourseId=  @CourseId
"""


sql_get_students = """
SELECT
  s.studentId
, s.FirstName
, s.FamilyName
 FROM school.course AS c
INNER JOIN 
school.student2course AS sc
ON c.courseId = sc.courseId
INNER JOIN 
school.student AS s
ON sc.studentId = s.studentId
WHERE
c.CourseId = @CourseId
"""

query_get_max_course_id = """
SELECT CASE WHEN max(CourseId) IS NOT NULL THEN  max(CourseId) ELSE 0 END AS MaxCourseId
FROM school.course"""

sql_remove_student_from_course = """
DELETE school.student2course
WHERE StudentId = @StudentId 
      AND CourseId = @CourseId
"""




query_get_max_schedule_id = """
SELECT
CASE WHEN max(ScheduleId) IS NOT NULL THEN  max(ScheduleId) ELSE 0 END AS MaxScheduleId 
FROM school.schedule"""

        
class Course(Event):
    
    def __init__(self,start_date = None,
                 end_date = None,
                 capacity = None,
                 course_name = None,
                 credit = None,
                course_id = None):
        super().__init__(start_date, end_date, capacity)
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        

    def add(self):
        connect_db = ConnectToDataBase()
        max_course_id = connect_db.get_values(query_get_max_course_id)
        new_course_id = max_course_id['MaxCourseId'][0] + 1
        rows_to_insert = [
            {"CourseId":  int(new_course_id), "CourseName": self.course_name, 
             "StartDate": self.start_date, "EndDate": self.end_date,
             "Credit": self.credit, "Capacity": self.capacity,
             "InsertionDate": datetime.now()}]
        connect_db.insert_rows('school','course',rows_to_insert)
        
        
    def update(self):
        parameters={'CourseName': "STRING", "CourseId": "INT64"
           }
        values = [self.course_name, self.course_id]

        connect_db=ConnectToDataBase()    
        connect_db.run_query(sql_update_course,
                                parameters,
                               values)
    @staticmethod   
    def add_participant(course_id,student_id):
        rows_to_insert = [{"StudentId":  int(student_id), "CourseId": course_id }]
        connect_db = ConnectToDataBase()
        connect_db.insert_rows('school','student2course',rows_to_insert)
    @staticmethod
    def delete_participant(course_id,student_id):
        parameters={'CourseId': "INT64", "StudentId": "INT64"}
        values = [course_id, student_id]
        connect_db=ConnectToDataBase()    
        connect_db.run_query(sql_remove_student_from_course,
                             parameters,
                            values)

  
       

            
class Schedule():
    def __init__(self, course_id):
        self.course_id = course_id
    def add(self, start_hour, end_hour):
        connect_db = ConnectToDataBase()
        max_schedule_id = connect_db.get_values(query_get_max_schedule_id)
        new_schedule_id = max_schedule_id['MaxScheduleId'][0] + 1
        rows_to_insert = [
            {"CourseId":  int(self.course_id), "ScheduleId": int(new_schedule_id)}]
        connect_db.insert_rows('school','course2schedule',rows_to_insert)
        
        rows_to_insert = [
            {"ScheduleId":  int(new_schedule_id), 
             "StartHour":  start_hour, "EndHour": end_hour}]
        connect_db.insert_rows('school','schedule',rows_to_insert)



