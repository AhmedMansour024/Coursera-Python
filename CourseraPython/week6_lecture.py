
#                                   #--------------- For Loop Over Indices  ----------------

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.
    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats


def count_adjacent_repeats(s):
    '''(str) -> list
    
    Return the number of occurrences of a character in all the parameter
    
    pre-condtion = parameter must be 1 str 
    >>> count_adjacent_repeats('abccdeffggh')
    ['a = 1', 'b = 1', 'c = 2', 'd = 1', 'e = 1', 'f = 2', 'g = 2', 'h = 1']   
    '''
    repeats = []
    unique_chars = list(set(s))  # Get unique characters in the string
    unique_chars.sort()
    for char in unique_chars:
        count = s.count(char)
        repeats.append(f"{char} = {count}")

    return repeats

# s = 'abcabcabcabccc'
# s = 'abccdeffggh'
# print(count_adjacent_repeats(s))



def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1
    '''
    
    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item      



def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1
    '''
    
    last_item = L[-1]

    for i in range(len(L) - 1 ,0 ,-1):
        L[i] = L[i - 1]

    L[0] = last_item     

# L = ['a', 'b', 'c', 'd', 'e']   #----> L = ['e', 'a', 'b', 'c', 'd']
# shift_left(L)
# shift_right(L)
# print(L)         



            #--------------Parallel Lists and Strings--------------------

def sum_items(list1, list2):
    '''(list of number, list of number) -> list of number

    Return a new list in which each item is sum of the items 
    at the corresponding position of list1 and list2. 

    pre-condition: len(list1) == len(list2)

    sum_items([1, 2, 3] ,[2, 4, 2])
    [3, 6, 5]
    '''
    sum_list = []

    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])
    
    print(sum_list)
    return sum_list
    
list01 = [1, 2, 3]
list02 = [2, 4, 2]        
sum_items(list01, list02)



def count_matches(s1, s2):
    ''' (str, str) -> int
    
    Return the number of positions in s1 that contain the
    same character at the corresponding position of s2.
    
    Precondition: len(s1) == len(s2)
    
    count_matches('ate', 'ape')
    2
    count_matches('head', 'hard')
    2
    '''

    num_matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1
    print(num_matches)
    return num_matches

#if we use the function with lists           <-<-<-<-<-<-<-<-<-
s1 = ['a','s','d','f']
s2 = ['w','s','r','f']
count_matches(s1,s2)



            #-----------------------Nested Lists----------------

grades = [['Assignment 1', 80], ['Assignment 2', 90], ['Assignment 3', 70]]

all_list = [items for sublist in grades for items in sublist]   #to change it to 1 list
print(all_list)

#Examples:
grades[0]    #->->->->->->->['Assignment 1', 80]
grades[1]    #->->->->->->->['Assignment 2', 90]
grades[2]    #-> -> -> -> ->['Assignment 3', 70]

grades[0][0]      # 'Assignment 1'
grades[0][1]      #  80
grades[1][0]      # 'Assignment 2'
grades[1][1]      # 90
grades[2][0]      # 'Assignment 3'
grades[2][1]      # 70


def calculate_average(asn_grades):
    '''(list of list of [str, number]) -> float

    Return the avarage of the grades in asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''

    total = 0
    for items in asn_grades:
        total = total + items[1]

    return total/len(asn_grades)

print(calculate_average([['A1', 80], ['A2', 90]]))


             #-------------------------Nested Loops-------------------


for i in range(10, 13):
    for j in range(1, 5):
        print(i, j)
               
#Here is the output:
'''
10 1
10 2
10 3
10 4
11 1
11 2
11 3
11 4
12 1
12 2
12 3
12 4
'''

for metal in ['Li', 'Na']:
    for gas in ['F', 'Cl', 'Br']:
        print(metal + gas)

outer = ['a','b','c','d','e','f','g']
inner = [1,2,3,4,5]

t_list = []
for i in outer:
    for j in inner:
        #print(f"spam! = {i*j}", end=" ")
        #t_list.append(f"spam! = {i*j}")
        t_list.append('spam!')

print(t_list)
print(t_list.count('spam!'))


def averages_of_list(grades):
    '''
    (list of list of number) -> list of float

    Return a new list in which each item is the average of the grades
    in the inner list at the corresponding position of grades.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    for grades_list in grades:
        # Calculate the average of grades_list and append it to averages.
        total = 0
        for mark in grades_list:
            total = total + mark
        averages.append(total / len(grades_list))

    return averages

list_grades = [[70,75,85,50],[70,80,90,100],[80,100]]
print(averages_of_list(list_grades))



                   #----------------------------Reading Files--------------------


import tkinter.filedialog
flanders_name = tkinter.filedialog.askopenfilename()
# # or
flanders_name = '/Users/nabil/Documents/flanders.txt'  # = tkinter.filedialog.askopenfilename()
flanders_file = open(flanders_name ,'r')

line = flanders_file.readline()
while line != '':
    print(line, end='')
    print(line.strip())
    print(line, end='')
    print(line.rstrip('\n'))                       
    print(line)                 #real all file but with speaces ('\n')
    line = flanders_file.readline()

#print(flanders_file.read())

# print(flanders_file.readlines())

flanders_file.close()

words_list = [line.strip() for line in flanders_file.readlines()]
print(words_list)

cat_name = '/Users/nabil/Documents/cat.txt'
cat_file = open(cat_name, "r")

print(cat_file.readlines())

print(cat_file.read())

cat_string = cat_file.read()
print(cat_string[3])   #->->->-> '\n'
print(cat_string[4])   #->->->-> 'c'



               #------------------------Writing Files--------------------------
'''
File dialogs:
Module tkinter has a submodule called filedialog. We import it like this:

import tkinter.filedialog
Function askopenfilename asks the user to select a file to open:

tkinter.filedialog.askopenfilename()
This function returns the full path to the file, so we can use that when we call function open to open that file.

from_filename = tkinter.filedialog.askopenfilename()
Function asksaveasfilename asks the user to select a file to save to, and provides a warning if the file already exists.

to_filename = tkinter.filedialog.asksaveasfilename()
'''

'''
simpler explanation:   <-<-<------------------------
from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()

And we can open the file we want to write to and write the contents:
to_file = open(to_filename, 'w')
to_file.write('Copy\n')  # We have to add the newline ourselves.
to_file.write(contents)  # Now write the contents of the file.
to_file.close()
'''



import tkinter.filedialog
tkinter.filedialog.askopenfilename()
from_filename = tkinter.filedialog.askopenfilename()
print(from_filename)

to_filename = tkinter.filedialog.asksaveasfilename()
print(to_filename)

from_filename = open(from_filename,'r')
contents = from_filename.read()
from_filename.close()
print(contents)

to_file = open(to_filename, 'w')
to_file.write("copy\n")
to_file.write(contents)
to_file.close()



import tkinter.filedialog       
cat_filename = tkinter.filedialog.askopenfilename()
print(cat_filename)

catlines = ["We looked! ", "And we saw him! ", "The Cat in the Hat! "]
cat_file = open(cat_filename, "w")
for line in catlines:
    cat_file.write(line)
cat_file.close() 


