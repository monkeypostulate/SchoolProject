import pytest
from school._business_rules import  ValidateStudentInformation, ValidateCourseInformation, ValidateSchedule,ValidateStudentCourseInfo


# #######        
# Check grade info 
def test_valid_grade():
    check_grade = ValidateStudentCourseInfo()
    assert check_grade.valid_grade('F')
    

def test_invalid_grade():
    check_grade = ValidateStudentCourseInfo()
    with pytest.raises(Exception) as e_info:
        check_grade.valid_grade(5)

# #######        
# Check student information  
#name
def test_valid_student_name():
    check_name = ValidateStudentInformation()
    assert check_name.check_student_names(first_name='Abel', family_name='Camacho')
        
def test_invalid_student_name():
    check_name = ValidateStudentInformation()
    with pytest.raises(Exception) as e_info:
        check_name.check_student_names(first_name='', family_name='Camacho')   
        
def test_invalid_student_name2():
    check_name = ValidateStudentInformation
    with pytest.raises(Exception) as e_info:
        check_name.check_student_names(first_name='Abel', family_name='') 

# capacity
def test_valid_capacity():
    check_name = ValidateStudentInformation()
    assert check_name.check_cedit_capacity(3)

def test_invalid_capacity():
    check_name = ValidateStudentInformation
    with pytest.raises(Exception) as e_info:
        check_name.check_cedit_capacity(50) 


# #######        
# Check course information  
def test_valid_credit():
    check_name = ValidateCourseInformation()
    assert check_name.check_credit(3)

def test_invalid_credit():
    check_name = ValidateStudentInformation
    with pytest.raises(Exception) as e_info:
        check_name.check_credit(50) 

# capacity      
def test_valid_capacity():
    check_name = ValidateCourseInformation()
    assert check_name.check_capacity(3)

def test_invalid_capacity():
    check_name = ValidateStudentInformation
    with pytest.raises(Exception) as e_info:
        check_name.check_capacity(50) 
        

# date      
def test_valid_date():
    check_name = ValidateCourseInformation()
    assert check_name.validate_date('2021-02-01')

def test_invalid_date():
    check_name = ValidateStudentInformation
    with pytest.raises(Exception) as e_info:
        check_name.validate_date('3') 

def test_invalid_date2():
    check_name = ValidateStudentInformation
    with pytest.raises(Exception) as e_info:
        check_name.validate_date('2021-02-31') 
        
# #######        
# Check Not overlapping schedule  
def test_non_overlapping_schedule():
    check_overlap = ValidateSchedule()
    assert check_overlap.non_overlap_schedule(
        start_date = '2021-04-01',
        end_date = '2022-01-01',
        start_hour =0,
        end_hour = 24,
        student_id = 1)
    
def test_overlapping_schedule():
    check_overlap = ValidateSchedule
    with pytest.raises(Exception) as e_info:
        check_overlap.non_overlap_schedule(
            start_date = '2021-01-01',
            end_date = '2022-01-01',
            start_hour =0,
            end_hour = 24,
            student_id = 1)
        
def test_overlapping_schedule2():
    check_overlap = ValidateSchedule
    with pytest.raises(Exception) as e_info:
        check_overlap.non_overlap_schedule(
            start_date = '2021-01-16',
            end_date = '2021-01-16',
            start_hour =0,
            end_hour = 24,
            student_id = 1)
        
        
def test_overlapping_schedule3():
    check_overlap = ValidateSchedule
    with pytest.raises(Exception) as e_info:
        check_overlap.non_overlap_schedule(
            start_date = '2020-01-01',
            end_date = '2022-01-01',
            start_hour =11,
            end_hour = 12,
            student_id = 1)
        
        
# ################################
#
# ################################

# valid grade
test_valid_grade()
test_invalid_grade()

# valid student info
test_valid_student_name()
test_invalid_student_name()
test_invalid_student_name2()

test_valid_capacity()
test_invalid_capacity()

# valid course info
test_valid_credit()
test_invalid_credit()

test_valid_capacity()
test_invalid_capacity()

test_valid_date()
test_invalid_date()
test_invalid_date2()


# Non overlapping schedules
test_non_overlapping_schedule()

# test_overlapping_schedule()
#test_overlapping_schedule2()
# test_overlapping_schedule3()