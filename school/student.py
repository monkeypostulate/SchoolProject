from school._student import Student
from school.student_information import StudentInformation
from school._business_rules import ValidateStudentInformation



  
class SchoolStudent():
    
    def __init__(self):
        pass
    
    @staticmethod
    def student(first_name = None,
                family_name = None,
                credit_capacity = None,
               student_id = None, 
               remove_student = False):
        
        student = Student(first_name = first_name,
                                family_name = family_name,
                                credit_capacity = credit_capacity)
        if student_id == None:
            validate_info = ValidateStudentInformation()
            validate_info.check_student_names(first_name,
                                             family_name)
            validate_info.check_credit_capacity(credit_capacity)
            student.create()
            print('New student added')
            return True

                   
        if student_id != None and remove_student == False:
            validate_info = ValidateStudentInformation()
            validate_info.check_student_names(first_name,
                                             family_name)
            student.update_info(student_id)
            print('student info updated')
            return True
        
        
        if student_id != None and remove_student == True:
            student.delete(student_id)
            print('student removed')
            return True
                      
    @staticmethod
    def student_information(student_id = None,
                            course_id = None,
                            student_information = None):
        get_student_info = StudentInformation(student_id = student_id)
        if student_information == 'all courses':
            return get_student_info.get_courses()
        
        elif student_information == 'course grade':
            return get_student_info.get_course_grade(course_id = course_id)
        
        if student_information == 'student average':
            return get_student_info.get_average_grade()
    