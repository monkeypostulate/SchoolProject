from database.connect_to_database import ConnectToDataBase
from school._business_rules import ValidateStudentCourseInfo


sql_update_grade="""
UPDATE 
school.student_grade
SET
Grade = @Grade
WHERE StudentId=  @StudentId
"""



class Grade():
    def __init__(self, course_id):
        self.course_id = course_id
    def add(self,
                          student_id = None,
                          grade = None):
        check_grade_logic = ValidateStudentCourseInfo()
        check_grade_logic.valid_grade(grade)
        check_grade_logic.valid_student_in_course(course_id = self.course_id, student_id = student_id)
        
        rows_to_insert = [{"CourseId":  int(self.course_id),
                           "StudentId": int(student_id),
                           "Grade": grade}]

        connect_db = ConnectToDataBase()
        connect_db.insert_rows('school','student_grade',rows_to_insert)
        
        
    def update(self,
                             student_id = None,
                          grade = None):

        connect_db=ConnectToDataBase()    

        parameters={'CourseId': "INT64", "StudentId": "INT64", "Grade":"STRING"}
        values = [self.course_id,student_id,grade]

        connect_db.run_query(sql_update_grade, parameters,values)
    def course_average_grade(self):
        pass
    @staticmethod
    def student_average_grade(student_id):
        pass
