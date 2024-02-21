# grade1=75
# grade2=65

# def garade_statue(grade1, grade2):
#     '''(num ,num) -> num
    
#     return the avarage of grades if passed in both subject and 
#     return passed grade if passed in one grade and
#     return 0.0 if not passed in both. ''' 

# #accemulatores for grades
# total = 0
# grade_count = 0


# if grade1 >= 50 and grade2 >= 50:
#     total = grade1 + grade2
#     grade_count = 2

# if grade_count > 0:
#     print(total / grade_count)
# else:
#     print(0.0)
# ####################    

# if grade1 >= 50:
#     total = total + grade1
#     grade_count = grade_count + 1
# else:
#     total = total + grade2
#     grade_count = grade_count + 1

# if grade_count > 0:
#     print(total / grade_count)
# else:
#     print(0.0)
# ####################

# if grade1 >= 50:
#     total = total + grade1
#     grade_count = grade_count + 1
# elif grade2 >= 50:
#     total = total + grade2
#     grade_count = grade_count + 1

# if grade_count > 0:
#     print(total / grade_count)
# else:
#     print(0.0)
    
# ###############
# if grade1 >= 50:
#     total = total + grade1
#     grade_count = grade_count + 1
# if grade2 >= 50:
#     total = total + grade2
#     grade_count = grade_count + 1

# if grade_count > 0:
#     print(total / grade_count)
# else:
#     print(0.0)    



'if we use a list for this example'

grade_list = []


    
def avr_grades_list(grades):
    '''([list]) -> number

    >>>avr_grades_list([30, 45, 60, 75, 70])
    total_avarage = 56.0
    failed_grade = (30, 45)
    '''
    passed_grades = [grade for grade in grades if grade >= 50]
    failed_grades = [grade for grade in grades if grade < 50]
    #print(passed_grades)
    #print(failed_grades)
    if len(passed_grades) >= len(failed_grades) and len(failed_grades) != 0:
        total_average = sum(passed_grades) / len(passed_grades)
        return f"Total average: {total_average:.2f}, Failed subjects: {failed_grades}"      
    elif len(passed_grades) <= len(failed_grades):
            return f"failed subject more then passed subject : {failed_grades}"
    elif len(failed_grades) == 0:
            total_average = sum(passed_grades) / len(passed_grades)
            return f"Total average: {total_average:.2f}, No failed subjects"
    else:
        return "Failed all subjects"

# Example usage:
grades_list = [75, 60, 90, 35, 80, 66, 55]
result = avr_grades_list(grades_list)
print(result)    #Total average: 67.50, Failed subjects: [40, 35, 25]

