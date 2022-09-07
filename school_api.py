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
@app.route('/school-api/v1/student/course', methods=['GET'])
def get_students_info():

    if 'studentId' in request.args:
        studentId = int(request.args['studentId'])
    else:
        return """
        <h2> Error: </h2> <p>
    No studentId field provided. </p>"""

    results = []
    get_courses = SchoolStudent()
    all_courses =get_courses.student_information(student_id = studentId, student_information = 'all courses')
    for i in range(all_courses.shape[0]):
        results.append(json.loads( all_courses.iloc[i].to_json()) )
    if len(results)>0:
        return results
    else:
        return """<h1>Error</h1>
    <p> No results found </p>"""

# Get student average grade information
@app.route('/school-api/v1/student/average-grade', methods=['GET'])
def get_students_avg_grade():

    if 'studentId' in request.args:
        studentId = int(request.args['studentId'])
    else:
        return """
        <h2> Error: </h2> <p>
    No student_id field provided. </p>"""

    results = []
    get_courses = SchoolStudent()
    all_courses =get_courses.student_information(student_id = studentId, student_information = 'student average')
    for i in range(all_courses.shape[0]):
        results.append(json.loads( all_courses.iloc[i].to_json()) )
    return results


# Get student course  grade information
@app.route('/school-api/v1/student/course-grade', methods=['GET'])
def get_students_course_grade():

    if 'studentId' in request.args and 'courseId' in request.args:
        studentId = int(request.args['studentId'])
        courseId = int(request.args['courseId'])
    else:
        return """
        <h2> Error: </h2> <p>
    No student_id or course_id field provided. </p>"""

    results = []
    get_courses = SchoolStudent()
    all_courses =get_courses.student_information(
        student_id = studentId,
        course_id = courseId,
        student_information = 'course grade')
    for i in range(all_courses.shape[0]):
        results.append(json.loads( all_courses.iloc[i].to_json()) )
    return results


##############################################
# Add a student to the school
@app.route('/school-api/v1/student/create', methods=['GET','POST'])
def set_students_info():
    if 'credit_capacity' in request.args:
        firstName = request.args['firstName']
        familyName = request.args['familyName']
        creditCapacity = int(request.args['creditCapacity'])
    else:
        return "Error: No credit_capacity field provided."
    
    SchoolStudent.student(first_name = firstName,
                        family_name = familyName,
                        credit_capacity = creditCapacity)
    return "<p> Succesfully added a new student  </p>"


##############################################
# Update student information
@app.route('/school-api/v1/student/update',
           methods=['GET','POST'])
def update_students_info():
    if 'studentId' in request.args and 'firstName' in request.args and 'family_name' in request.args:
        studentId = request.args['studentId']
        firstName = request.args['firstName']
        familyName = request.args['familyName']
    else:
        return """
        <h2> Error:</h2>
        <p>student_id, family_name or first_name information missing</p>"""
    
    SchoolStudent.student(
        student_id= studentId,
        first_name = firstName,
        family_name = familyName,
        credit_capacity = creditCapacity)
    return "<p> Succesfully updated student info.  </p>"




##############################################
# Add a student to the school
@app.route('/school-api/v1/course/create', methods=['GET','POST'])
def set_course_info():
    if 'course_name' in request.args:
        course_name = request.args['courseName']
        start_date = request.args['startDate']
        end_date = request.args['endDate']
        credit = request.args['credit']
        capacity =request.args['capacity']
    else:
        return """
        <h2>Error:</h2>
        <p>Information missing.</p>"""

    SchoolCourse.course(course_name = courseName,
                     start_date = startDate,
                     end_date = endDate,
                     credit = int(credit),
                     capacity = int(capacity) )
    return "<p> Succesfully added a new course  </p>"



##############################################
# Add a student to  course
@app.route('/school-api/v1/course/add-student', methods=['GET','POST'])
def insert_student2course():
    if 'studentId' in request.args and 'courseId' in request.args:
        studentId = request.args['studentId']
        courseId = request.args['courseId']
    else:
        return """
        <h2>Error:</h2>
        <p>Information missing.</p>"""

    student2course = StudentInCourse(student_id = studentId )
    student2course.add_student_to_course( course_id = courseId)
    return "<p> Succesfully added student to  course  </p>"




##############################################
# Add student's grade
@app.route('/school-api/v1/course/student-grade/insert', methods=['GET','POST'])
def add_student_grade():
    if 'studentId' in request.args and 'courseId' in request.args:
        student_id = request.args['studentId']
        course_id = request.args['courseId']
        grade = request.args['grade']
    else:
        return """
        <h2>Error:</h2>
        <p>Information missing.</p>"""
    add_grade = Grade(course_id = course_id)
    add_grade.add(student_id = studentId, grade = grade)

    return "<p> Succesfully added student's grade  </p>"



if __name__ == '__main__':
    app.run(host="localhost", port=8787, debug=True)

app.run()

