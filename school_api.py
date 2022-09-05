from  school.student import Student
from school.course import SchoolCourse
from school.student_course import StudentInCourse
from school.student import SchoolStudent
from school.grade import Grade

import flask
from flask import request, jsonify

import pandas
import json





app = flask.Flask(__name__)
app.config["DEBUG"] = True


##############################################
# API information
@app.route('/', methods=['GET'])
def home():
    return """<h1>School API</h1>
<p>This site is a prototype API for the school project</p>
"""


##############################################
# Get student course information
@app.route('/api/v1/resources/student/info', methods=['GET'])
def get_students_info():

    if 'student_id' in request.args:
        student_id = int(request.args['student_id'])
    else:
        return """
        <h2> Error: </h2> <p>
    No student_id field provided. </p>"""

    results = []
    get_courses = SchoolStudent()
    all_courses =get_courses.student_information(student_id = student_id, student_information = 'all courses')
    for i in range(all_courses.shape[0]):
        results.append(json.loads( all_courses.iloc[i].to_json()) )
    return results

# Get student average grade information
@app.route('/api/v1/resources/student/average-grade', methods=['GET'])
def get_students_avg_grade():

    if 'student_id' in request.args:
        student_id = int(request.args['student_id'])
    else:
        return """
        <h2> Error: </h2> <p>
    No student_id field provided. </p>"""

    results = []
    get_courses = SchoolStudent()
    all_courses =get_courses.student_information(student_id = student_id, student_information = 'student average')
    for i in range(all_courses.shape[0]):
        results.append(json.loads( all_courses.iloc[i].to_json()) )
    return results


# Get student course  grade information
@app.route('/api/v1/resources/student/course-grade', methods=['GET'])
def get_students_course_grade():

    if 'student_id' in request.args and 'course_id' in request.args:
        student_id = int(request.args['student_id'])
        course_id = int(request.args['course_id'])
    else:
        return """
        <h2> Error: </h2> <p>
    No student_id or course_id field provided. </p>"""

    results = []
    get_courses = SchoolStudent()
    all_courses =get_courses.student_information(
        student_id = student_id,
        course_id = course_id,
        student_information = 'course grade')
    for i in range(all_courses.shape[0]):
        results.append(json.loads( all_courses.iloc[i].to_json()) )
    return results


##############################################
# Add a student to the school
@app.route('/api/v1/resources/student/create', methods=['GET','POST'])
def set_students_info():
    if 'credit_capacity' in request.args:
        first_name = request.args['first_name']
        family_name = request.args['family_name']
        credit_capacity = int(request.args['credit_capacity'])
    else:
        return "Error: No credit_capacity field provided."
    
    SchoolStudent.student(first_name = first_name,
                        family_name = family_name,
                        credit_capacity = credit_capacity)
    return "<p> Succesfully added a new student  </p>"


##############################################
# Update student information
@app.route('/api/v1/resources/student/update',
           methods=['GET','POST'])
def update_students_info():
    if 'student_id' in request.args and 'first_name' in request.args and 'family_name' in request.args:
        student_id = request.args['student_id']
        first_name = request.args['first_name']
        family_name = request.args['family_name']
    else:
        return """
        <h2> Error:</h2>
        <p>student_id, family_name or first_name information missing</p>"""
    
    SchoolStudent.student(
        student_id= student_id,
        first_name = first_name,
        family_name = family_name,
        credit_capacity = credit_capacity)
    return "<p> Succesfully updated student info.  </p>"




##############################################
# Add a student to the school
@app.route('/api/v1/resources/course/create', methods=['GET','POST'])
def set_course_info():
    if 'course_name' in request.args:
        course_name = request.args['course_name']
        start_date = request.args['start_date']
        end_date = request.args['end_date']
        credit = request.args['credit']
        capacity =request.args['capacity']
    else:
        return """
        <h2>Error:</h2>
        <p>Information missing.</p>"""

    SchoolCourse.course(course_name = course_name,
                     start_date = start_date,
                     end_date = end_date,
                     credit = int(credit),
                     capacity = int(capacity) )
    return "<p> Succesfully added a new course  </p>"



##############################################
# Add a student to  course
@app.route('/api/v1/resources/student2course/insert', methods=['GET','POST'])
def insert_student2course():
    if 'student_id' in request.args and 'course_id' in request.args:
        student_id = request.args['student_id']
        course_id = request.args['course_id']
    else:
        return """
        <h2>Error:</h2>
        <p>Information missing.</p>"""

    student2course = StudentInCourse(student_id = student_id )
    student2course.add_student_to_course( course_id = course_id)
    return "<p> Succesfully added student to  course  </p>"




##############################################
# Add student's grade
@app.route('/api/v1/resources/student-grade/insert', methods=['GET','POST'])
def add_student_grade():
    if 'student_id' in request.args and 'course_id' in request.args:
        student_id = request.args['student_id']
        course_id = request.args['course_id']
        grade = request.args['grade']
    else:
        return """
        <h2>Error:</h2>
        <p>Information missing.</p>"""
    add_grade = Grade(course_id = course_id)
    add_grade.add(student_id = student_id, grade = grade)

    return "<p> Succesfully added student's grade  </p>"



if __name__ == '__main__':
    app.run(host="localhost", port=8787, debug=True)

app.run()

