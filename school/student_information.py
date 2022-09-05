from school.connect_to_database import ConnectToDataBase



sql_get_courses = """
SELECT
c.CourseName
FROM 
school.student AS s
INNER JOIN
school.student2course AS sc
ON s.StudentId = sc.StudentId
INNER JOIN
school.course AS c
ON sc.CourseId = c.CourseId
WHERE 
s.StudentId = @StudentId
"""

sql_get_course_grade = """
SELECT
s.FirstName
,s.FamilyName
,sg.Grade
,c.CourseName
FROM 
school.student AS s
INNER JOIN
school.student_grade AS sg
ON s.StudentId = sg.StudentId
INNER JOIN
school.course AS c
ON sg.CourseId = c.CourseId
WHERE
s.StudentId = @StudentId
AND c.CourseId = @CourseId
"""

sql_get_student_avergage_grade = """
SELECT
s.FirstName
,s.FamilyName
,AVG(g.GradeNumeric) AS AverageGrade
FROM 
school.student AS s
INNER JOIN
school.student_grade AS sg
ON s.StudentId = sg.StudentId
INNER JOIN
school.grades AS g
ON sg.Grade = g.Grade
WHERE
s.StudentId = @StudentId
GROUP BY 
1,2
"""

class StudentInformation():
    def __init__(self, student_id):
        self.student_id = student_id
    def get_courses(self):
        connect_db=ConnectToDataBase() 
        parameters={ "StudentId": "INT64"
           }
        values = [self.student_id]
        results = connect_db.run_query(sql_get_courses,
                                          parameters,
                                          values)
        return results.to_dataframe()
      
    def get_course_grade(self, course_id):
        connect_db=ConnectToDataBase()
        parameters={ "StudentId": "INT64","CourseId": "INT64"
           }
        values = [self.student_id,course_id]
        results = connect_db.run_query(sql_get_course_grade,
                                          parameters,
                                          values)
        return results.to_dataframe()
    
    def get_average_grade(self):
        connect_db=ConnectToDataBase()
        parameters={ "StudentId": "INT64"}
        values = [self.student_id]
        results = connect_db.run_query(sql_get_student_avergage_grade,
                                       parameters,
                                       values)
        return results.to_dataframe()


