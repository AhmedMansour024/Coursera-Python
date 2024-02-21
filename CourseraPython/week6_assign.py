def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        #print(i)
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))

             ############################################################################


def mystery(s):      #2 times right                 
    """ (str) -> bool
    """
    matches = 0
    print(len(s)//2)
    for i in range(len(s) // 2):
        print(len(s))
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

print(mystery('civillivic'))
print(mystery('1234554321'))

l = 'civillivic'
print(l[9])

               ####################################################################


def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    for i in range(len(L) - 1):
        L[i] = L[i + 1]
    
    for i in range(len(L)):
        L[i + 1] = L[i]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
    
    for i in range(1, len(L)):
        L[i] = L[i + 1]
    
    L[0] = last_item


L = ['a', 'b', 'c', 'd', 'e']   #----> L = ['e', 'a', 'b', 'c', 'd']
shift_right(L)
print(L)

                 #######################################################################

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with
    the string from thecorresponding position of list1 and 
    the int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''
    pairs = []
    # CODE MISSING HERE
    inner_list = []
    for i in range(len(list1)):              #<-----
        pairs.append([list1[i], list2[i]])


    inner_list = []
    for i in range(len(list1)):
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
    
    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
    pairs.append(inner_list)

    for i in range(len(list1)):            #<----
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs

print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))

def two_loops(x,y,z,x)
    for i in range(x, y):
        for j in range(z, x):
            print(i, j)



def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False  # We have not yet found value in the list.

    ## CODE MISSING HERE
    # for i in range(len(lst)):
    #     for j in range(len(lst[i])):
    #         if lst[i][j] == value:
    #             found = True

    for sublist in lst:
        if value in sublist:
            found = True
    
    # for i in range(len(lst)):
    #     for j in range(len(lst[i])):
    #         found = (lst[i][j] == value)

    return found

print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],[80, 100]]))


# Q10:               make this code
# A file has a section at the top that has a preamble describing the contents of the file, 
# then a blank line,
# then a list of high temperatures for each day in January all on one line,
# then a list of high temperatures for each day in February all on one line,
# then lists for March, April, and so on through December, each on one line.  
# There are thousands of lines of information after that temperature data that you aren't currently interested in.

# You want to write a program that prints the average of the high temperatures in January. 
# Which of the four file-reading approaches should you use?

# Hint: review the Reading Files lecture.

# The readline approach

# The for line in file approach

# The readlines approach

# The read approach

# import tkinter.filedialog

# Q_10_name = '/Users/nabil/Documents/week6 assign Q10.txt' #tkinter.filedialog.askopenfilename()
# Q_10_file = open(Q_10_name, 'r')

# print(Q_10_file.readlines()[6])

# Q10: solve:           <<--------------------------------------------
# Q10:
# A file has a section at the top that has a preamble describing the contents of the file, 
# then a blank line,
# then a list of high temperatures for each day in January all on one line,
# then a list of high temperatures for each day in February all on one line,
# then lists for March, April, and so on through December, each on one line.  
# There are thousands of lines of information after that temperature data that you aren't currently interested in.

# You want to write a program that prints the average of the high temperatures in January. 


import tkinter.filedialog
file_name = tkinter.filedialog.askopenfilename()
file_P = open(file_name, 'r')

def ave_temp_month(file_name, month):
    '''(file open for reading, str) -> float
    Return the average of the high temperatures in a month of year.

    pre-condition: A file has a section at the top that has a preamble describing the contents of the file, 
    then a blank line,then a list of high temperatures.

    >>>ave_temp_month(file, month)
    40.0
    '''
    temp_list = []
    for line in file_name:
        if line.startswith(month):
            temp_line = file_name.readline().strip().split()   #list = ['32', '34', '36', '33'....']
            for num in temp_line:
                temp_list.append(int(num))
                #print(temp_list)                              #list = [32, 34, 36, 33, 30,....]
            ave_temp = sum(temp_list) / len(temp_list)
            return f'average of the high temperatures in {month} = {ave_temp}'
            #return ave_temp
        
               
print(ave_temp_month(file_P, 'January'))
        


data = "January: 32 34 36 33 30 29 31 30 32 35 37 38 40 39 36 35 34 32 30 31 33 35 36 38 39 40 41 42 43 41"

# Finding the index of the colon
colon_index = data.find(':')

# Extracting the temperatures for January
january_temperatures = data[colon_index + 1:].split()

print(january_temperatures)



def get_temperatures_for_month(file_name, month):
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith(month):
                colon_index = line.find(':')
                temperatures = line[colon_index + 1:].split()
                return temperatures

# Usage
file_name = 'temperature_data.txt'
requested_month = 'January'

january_temperatures = get_temperatures_for_month(file_name, requested_month)
print(f"Temperatures for {requested_month}: {january_temperatures}")




# Q11 
    # print(line, end='')
    # print(line.rstrip('\n'))    



# Q12:  wrong

def lines_startswith(file, letter):   
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter. 
    The lines should have the new line removed.

    Precondition: len(letter) == 1
    """

    matches = []

    # CODE MISSING HERE
    matches.append(line.startswith(letter).rstrip('\n'))

    for line in file:  #right
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
            
    for line in file:    #wrong because it searches for a letter through entire line and not only at the beginning of it
        if letter in line:
            matches.append(line.rstrip('\n'))

    for line in file:   #right
        if line.startswith(letter):
            #matches.append(line.rstrip('\n'))
            while line != '\n':
                matches = list(file.readlines())

    return matches

flanders_name = '/Users/nabil/Documents/week6 assign Q10.txt' #tkinter.filedialog.askopenfilename()
file = open(flanders_name, 'r')


flanders_name = '/Users/nabil/Documents/flanders.txt'
file = open(flanders_name ,'r')

letter = 'January'
print(lines_startswith(file, letter))



def lines_startswith(file, letter):       #chatgpt
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter. 
    The lines should have the new line removed.

    Precondition: len(letter) == 1
    """

    matches = []

    for line in file:
        if line.startswith(letter):
            # Remove the newline character and append the line to matches
            matches.append(line.rstrip('\n'))

    return matches



def write_to_file(file, sentences):   
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
    for s in sentences:
        file.write(s)
        file.write('\n')


    
    for s in sentences:
        file.write(s + '\n')
