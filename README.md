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


![image](https://user-images.githubusercontent.com/25433668/188940537-936b575f-2e23-47c9-aa71-e24f3b5fe184.png)

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
http://localhost:8787/school-api/v1/student/data?student_id=11
```

Results is a json file.
If there is a student with the given student_id, then the results looks like

![image](https://user-images.githubusercontent.com/25433668/188947099-3de50142-8709-48bf-b736-1df08edf0792.png)

If there is no student, then we get an empty set.

![image](https://user-images.githubusercontent.com/25433668/188947317-36a8ca92-d8b5-4308-970d-f5dea05a1fed.png)

If the wrong parameter is provided, the following error occurs:
![image](https://user-images.githubusercontent.com/25433668/188947512-801a5df5-d3c1-4836-893f-968e4ab55806.png)

Othe functionalities of the API are

* Get all courses from a student
```
http://localhost:8787/school-api/v1/student/course?studentId=1
```

* Get the average grade of a student
```
http://localhost:8787/school-api/v1/student/average-grade?studentId=1
```

* Get student's grade of a course.
```
http://localhost:8787/school-api/v1/student/course-grade?studentId=1
```

* Create a student
```
http://localhost:8787/school-api/v1/student/create?familyName=Camacho%firstName=Abel&creditCapacity=10
```



* Update the information of a student
```
http://localhost:8787/school-api/v1/student/update?studentId=1&familyName=Camacho&firstName=Leo
```

*  Create a course.
```
http://localhost:8787/school-api/v1/student/data?courseName=Calculus&startDate=2021-01-01&endDate=2021-01-10&capacity=3&credit=3
```


*  Add a student to a  course.
```
http://localhost:8787/school-api/v1/course/add-student?studentId=1&courseId=1
```

