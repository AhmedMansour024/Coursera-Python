import tkinter.filedialog
import grade

# import sys
# # Insert the directory path containing the file to be imported
# sys.path.insert(1, r'C:\Users\nabil\Documents')
# # Now you can import the file
# import grade  


# or
# import filename

# If your python file is inside another folder, then you need to create a blank __init__.py file 
# that will help python to understand it's a package. Then you can import that as follows:
# from folderName import filename

def main():
    a1_filename = tkinter.filedialog.askopenfilename()
    a1_file = open(a1_filename, 'r')

    a1_histfilename = tkinter.filedialog.askopenfilename()
    a1_histfile = open(a1_histfilename, 'w')


    ###Read thegrades into a list:
    grades = grade.read_grades(a1_file)

    #count the grades per range:
    range_counts = grade.count_grade_ranges(grades)

    #write the histogram to the file:
    grade.write_histogram(range_counts, a1_histfile)

    a1_file.close()
    a1_histfile.close()
    return 0


# ---------------------------------------
grade1=75
grade2=65

# def garade_statue(grade1, grade2):
#     '''(num ,num) -> num
    
#     return the avarage of grades if passed in both subject and 
#     return passed grade if passed in one grade and
#     return 0.0 if not passed in both. ''' 

# accemulatores for grades
total = 0
grade_count = 0


if grade1 >= 50 and grade2 >= 50:
    total = grade1 + grade2
    grade_count = 2

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
####################    

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
####################

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
elif grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)
    
###############
if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
if grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)    



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


    
if __name__=="__main__":
    main()