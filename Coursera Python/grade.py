def read_grades(gradefile):
    '''(file open for reading) -> list of float

    read and return the list of grades in gradefile.

    precondition: gradefile starts with a header that contain no blank lnes,
    then has a blank line, and then lines containing a student number and a grade.
    '''

    # skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # read the grades, accumulating them into a list.

    grades = []
    
    line = gradefile.readline()
    while line != '':
        # now we have s string containing the info for a single student.
        # find the last space and take everything after that space.
        grade = line[line.rfind(' ') + 1 :]
        grades.append(float(grade))
        line = gradefile.readline()

    return grades
        


def count_grade_ranges(grades):
    '''(list) -> (list)

    return list of intwhere each index indicates how many grades were in these ranges:

    0-9:   1
    10-19: 2
      :
    90-99: 9
    100:   10

    >>> count_grade_ranges([90.8, 67.8, 54.6, 69.2, 63.9, 65.2, 59.2, 67.8, 59.6, 76.2])
    [0, 0, 0, 0, 0, 3, 5, 1, 0, 1, 0]
    
    '''

    range_counts = [0] *11
    for grade in grades:
        which_range = int(grade // 10)
        range_counts[which_range] = range_counts[which_range] + 1
        
    return range_counts    



def write_histogram(range_counts, histfile):
    '''(list of int, file open for wirting) -> Nonetype

    write histogram of *`s based on the number of grades in each range.

    the output format:
    0-9:   **
    10-19: ***
    20-29: *****
      :
    90-99: *  
    100:   **
    '''

    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')
    
    #write the 2-digit ranges.
    for i in range(1, 10):
        low = i * 10
        high = (i *10) + 9 
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        histfile.write('\n')
        
    histfile.write('100: ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')

