from school.connect_to_database import ConnectToDataBase




class StudentInCourse():
    def __init__(self, student_id):
        self.student_id = student_id
    def add_student_to_course(self, course_id):
        rows_to_insert = [
            {"StudentId":  int(self.student_id), "CourseId": course_id
            }]
        connect_db = ConnectToDataBase()
        connect_db.insert_rows('school','student2course',rows_to_insert)
    
    def remove_student_to_course(self, course_id):
        connect_db = ConnectToDataBase()
        parameters={'CourseId': "INT64", "StudentId": "INT64"}
        values = [course_id,self.student_id]
        connect_db.run_query("DELETE school.student2course WHERE StudentId = @StudentId AND CourseId = @CourseId",
                             parameters,
                            values)