<h1>
Course Project: Student Course Assignment Service
</h1>
<h3>
Author: Abel Camacho Guardian
</h3>

<br>

 

### Database

The database is done in BigQuery, and the files to create the tables are in the file create_database. An advantage of BigQuery is that it allows for fast reading of large datasets.
However, tables are not allow to have primary keys. 
Thus, the logic to define unique ids (e.g. student_id, course_id) is done in the school module.

Tables:
Each student is defined by a student_id, first_name, family_name, credit_capacity and status. 
A student can be removed from the school, but not from the database. When a student is removed from the school, then its status becomes 0. An active student has status 1.
<br>
A course is defined by a course_name, start_date, end_date, credit,  capacity (max number of students allowed).  Each course can have schedules, i.e. the time and day when the course take place.
The schedule table has the schedule information of all courses.
Students in a course are in the table student2course.
The grade of a student is in the table student_grade, and the grade is a string, e.g. A.
<br>
The table grade has the relationship between numeric and alphabetic grades.


![image](https://user-images.githubusercontent.com/25433668/188918168-7e86d037-82c8-4001-905d-7b47a96b3d25.png)


### Module school

The module school contains the classes and methods used for the API.
<br>
In the file example, we show how we can create students and courses.
We also show how to add students to a course, or add a grade to a student.

### Module database

The module database has all the functionalities to connect to the database.


### School API
The school api was tested in a virtual machine in Google Cloud.
However, it is currently only accesible as a localhost due to security reasons. I haven't been able to make it accesible to the public. 
<br>
The school api is in the file school.api. It was written using the package Flask.
A challenge when using Flaks in the cloud is to have an port that I can use in my local machine. Fortunately, I already had the port 8787 open for a previous project (I needed for R-shiny on the cloud). Thus, I use the port 8787 and not the port 1024, as specified in the homework. 


### Testing
The tests are found in the folder tests. Currently, we only have tests for the business logic. 
For instance, we test if our method to restrict a student to attend two courses that occur at the same time works according to our logic.
A challenge in this section was to create my first tests, since I haven't done any unittesting before at work or during my studies.

```
pytest -q test_business_rules.py
```
Currently, there are 19 tests.
<br>
![image](https://user-images.githubusercontent.com/25433668/188721697-6ff25a0f-757e-4ad9-b81a-f1589c8d150f.png)


#### Examples of API

Student information can be retrieved as follow:
```
http://localhost:8787/api/v1/resources/student/info?student_id=1
```
Results is a json file.
If there is a student with the given student_id, then the results looks like

![image](https://user-images.githubusercontent.com/25433668/188919457-9f801a5e-1121-4f53-9917-2b8d340d5bb8.png)

If there is no student, then we get an empty set.

![image](https://user-images.githubusercontent.com/25433668/188919149-7ed3f666-02e4-4904-bcfa-a98e9bb9a15f.png)


Othe functionalities of the API are get all courses from a student, get the average grade of a student, and get the grade of a course.
It is aslo possible to create a student, update the information of a student, and also create a course.


