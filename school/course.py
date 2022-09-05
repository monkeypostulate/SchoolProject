from school._course  import Course, Schedule
from school._business_rules import ValidateCourseInformation,ValidateStudentCourseInfo


  
        
class SchoolCourse():
    @staticmethod
    def course(course_name= None,
               start_date = None,
               end_date = None,
               credit = None,
               capacity = None,
               course_id = None,
               remove_course = False
                ):
        course = Course(course_name= course_name,
               start_date = start_date,
               end_date = end_date,
               credit = credit,
               capacity = capacity,
               course_id = course_id,
               )

        if course_id ==None:
            validate_info = ValidateCourseInformation()
            validate_info.check_credit(credit)
            validate_info.check_capacity(capacity)
            validate_info.validate_date(start_date)
            validate_info.validate_date(end_date)
            course.add()
            print('Course added')
        elif course_id != None and remove_course == False:
            
            course.update()
            print('Updated Course Information')
            True
        elif course != None and remove_course == True:
            False
    @staticmethod
    def student_to_course(student_id = None,
                             course_id = None,
                         action = 'add'):
        student_course = Course(course_id)
        validate_info = ValidateStudentCourseInfo()
        validate_info.check_student_course_exist(course_id = course_id,
                                   student_id = student_id)
        if action == 'add':
            student_course.add_participant(course_id = course_id,
                                           student_id = student_id)
        elif action == 'delete':
            student_course.delete_participant(course_id = course_id,
                                              student_id = student_id)
    
    @staticmethod
    def add_schedule(course_id,
                     start_hour,
                     end_hour):
        schedule = Schedule(course_id)
        schedul.add(start_hour,
                     end_hour)
        
       
    

    
class CourseInformation():
    def __init__(self, course_id):
        self.course_id = course_id
    def get_schedule():
        pass
    def get_students(self):

        parameters={'CourseId': "INT64"}
        values = [self.course_id]
        parameters=[['CourseId'],['INT64']] 
        connect_db=ConnectToDataBase()    
        results = connect_db.run_query(sql_get_students,
                                       parameters,
                                       values)
        return results.to_dataframe()

    def set_student_grade(self, student_id,grade):
        connect_db = ConnectToDataBase()
        rows_to_insert = [
            {"StudentId":  int(student_id), "CourseId": int(self.course_id),
             "Grade": grade}]
        connect_db.insert_rows('school','student_grade',rows_to_insert)
        



