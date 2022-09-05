from school.person import Person
from school.connect_to_database import ConnectToDataBase



sql_update_student="""
UPDATE 
`theoreticalmonkey.school.student`
SET
FirstName = @FirstName
,FamilyName = @FamilyName
WHERE StudentId=  @StudentId
"""


sql_delete_student="""
UPDATE 
`theoreticalmonkey.school.student`
SET
 Status = @Status
WHERE StudentId=  @StudentId
"""


             

class Student(Person):
    def __init__(self, 
                 student_id = None,
                 first_name =None,
                 family_name =None,
             credit_capacity=None):
        super().__init__(first_name, family_name)
        self.student_id = student_id
        self.first_name = first_name
        self.family_name = family_name
        self.credit_capacity = credit_capacity    

    def create(self):
        query_get_max_student_id = 'SELECT CASE WHEN max(StudentId) IS NOT NULL THEN  max(StudentId) ELSE 0 END AS MaxStudentId FROM school.student '
        connect_db = ConnectToDataBase()
        max_student_id = connect_db.get_values(query_get_max_student_id)
        new_student_id = max_student_id['MaxStudentId'][0] + 1
        rows_to_insert = [
            {"StudentId":  int(new_student_id), "FirstName": self.first_name,
             "FamilyName": self.family_name, "CreditCapacity": self.credit_capacity, 
             "Status": 1 }]
        connect_db.insert_rows('school','student',rows_to_insert)
        
    def update_info(self,student_id):
        parameters={'FirstName': "STRING","FamilyName": "STRING",
                         "StudentId": "FLOAT64"}
        values =[self.first_name, self.family_name,student_id]

        connect_db=ConnectToDataBase()    
        connect_db.run_query(sql_update_student,
                             parameters,
                            values)

    def delete(self,student_id):
        parameters={'Status': "FLOAT64","StudentId": "STRING",
                         "StudentId": "FLOAT64"}
        values =[0,student_id]

        connect_db=ConnectToDataBase()    
        connect_db.run_query(sql_delete_student,
                             parameters,
                            values)
        
        
    
  