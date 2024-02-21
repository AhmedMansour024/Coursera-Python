            #----------------------Tuples-----------------------

# Tuples are immutable sequences: they cannot be modified.
# Tuples and lists have much in common, but lists are mutable sequences: they can be modified.
# Tuples use parentheses () instead of square brackets []:
# General form of a tuple:
# (expr1, expr2, expr3, ....,expri)    
# For example:
lst = ['a', 3, -0.2]
tup = ('a', 3, -0.2)

# Once created, items in lists and tuples are accessed using the same notation:

lst[0]
# -> 'a'
tup[0]
# -> 'a'
lst[1]
# 3
tup[1]
# 3

# Slicing can be used with both:
lst[:2]
# -> ['a', 3]
tup[:2]
# -> ('a', 3)

# Tuples cannot be modified:
# tup[0] = 'b'                   -> TypeError: 'tuple' object does not support item assignment

# Tuples have fewer methods than lists. use >>> help()
# Lists have methods append, count, extend, index, insert, pop, remove, reverse, and sort. 
# But tuples only have count and index.

# Like lists, we can iterate over the items in a tuple.  -> using For loop
# tup = ('a', 3, -0.2)
for item in tup:
    print(item)

# a
# 3
# -0.2
    
# Function len, works on tuples.   -> len()   
len(tup)
# 3

# General form of a tuple:
# (expr1, expr2, expr3, ....,expri)    
# For example:
s = (1, 2)
s[0]
# 1
s[1]
# 2

# A tuple can be passed as an argument to the built-in function -->>(len)<<--:
len(tup)
# 3
# It is also possible to iterate over the indices of a tuple:
for i in range(len(tup)):
        print(tup[i])
# a
# 3
# -0.2 


              #--------------------Type dict-------------------

# Dictionary
# Another way to store collections of data is using Python's dictionary type: dict.

# The general form of a dictionary is:
# {key1: value1, key2: value2, ......, keyN: valueN}
        
# Keys must be unique. Values may be duplicated. 
        
# For example:
asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90}

# In the example above, the keys are unique: 'A1', 'A2' and 'A3'. 
# The values are not unique: 80, 90 and 90.

# To look up the grade associated with assignment A2, 
# we can use the bracket notation [] that we used with the nested list. 
# For example:
asn_to_grade['A2']     # --> 70

# If we try to access a list, and an index that does not exist an error occurs.
# For example:
# ---asn_to_grade['A4']      # --> TypeError

# we can check for the existence in the dictionary. 
# So we could have checked to see wether A4 is in asn_to_grade.
'A4' in asn_to_grade     # --> false
'A2' in asn_to_grade     # --> True

# The len built-in function, that trends the number of key-value pairs.
# For example:
len(asn_to_grade)        # --> 3

# Like lists, dictionaries are -( mutable ) <<<-, that means the key-value pairs can be added to a dictionary. 
# The value associated with the key could be changed and key-value pairs can be removed from a dictionary.
# For example:
asn_to_grade['A4'] = 85
len(asn_to_grade)         # --> 4

# Using the same notation we can also update the values associated with a key. 
# So for key A4. We're going change its value now from 85 to 90. 
# Because A4 already exists in the dictionary, this becomes a change. 
# If the key A4 didn't exist, like before, then the new key value pair would be added.
# For example:
asn_to_grade['A4'] = 90
print(asn_to_grade)      # --> {'A1': 80, 'A2': 90, 'A3': 90, 'A4': 90}

# Values can be duplicated, as mentioned before, but keys cannot.
# For example:
# asn_to_grade = {'A1': 80, 'A2': 90, 'A3': 90, 'A4': 90}     <<<----  
# in this example there is 3 of 90
# but there cannt be 3 'A1'

# remove a key value pair from the dictionary. 
# To do this we will use the operator del and then the dictionary reference and the key, using the same bracket notation. 
# For example:
del asn_to_grade['A4']
print(asn_to_grade)       # {'A1': 80, 'A2': 90, 'A3': 90}

# We can use a for loop to loop over the keys of a dictionary, 
# like we did to loop over the characters of a string, or the items of a list.
# For example:
for assignment in asn_to_grade:
      print(assignment)

# A1
# A2
# A3

# let's print the values.
# For example:
for assignment in asn_to_grade:
      print(asn_to_grade[assignment])      

# 80
# 90
# 90   

# to print Both.
# For example:
for assignment in asn_to_grade:
      print(assignment, asn_to_grade[assignment])  

# the type of keys must always be immutable.
# Since lists are mutable, a list cannot be used as a dictionary key.
# For example:
d = {}
#d[[1, 2]] = 'banana'       # TypeError

# we can use a tuple, because tuples are immutable.
# For example:
d[(1, 2)] = 'banana'       
print(d)                    # -> d = {(1, 2) : 'banana'}


                #----------------------Inverting a Dictionary----------------

                                    # Switching Keys and Values
# Dictionaries have keys that are unique and each key has a value associated with it.
# For example:
fruit_to_colour = {'watermelon': 'green', 'pomegranate': 'red',
'peach': 'orange', 'cherry': 'red', 'pear': 'green',
'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}

# To invert the dictionary, that is, switch the mapping to be colours to fruit.
# here is one approach: For example:
colour_to_fruit = {}
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    colour_to_fruit[colour] = fruit

print(colour_to_fruit)    
# ->>>{'orange': 'orange', 'purple': 'plum', 'green': 'pear', 'yellow': 'banana', 'red': 'pomegranate'}
# There are no pomegranates, no strawberries, no peaches. because they all have red colour.
# So, when we added a fruit with the same colour to this dictionary, it replaced the fruit that there.

# so to fix this, we need to consider two cases when adding a colour and a fruit to the dictionary:
# If the colour is not a key in the dictionary, add it with its value being a single element a list consisting of the fruit.
# If the colour is already a key, append the fruit to the list of fruit associated with that key.
# For example:
colour_to_fruit = {}
for fruit in fruit_to_colour:
    # What colour is the fruit?
    colour = fruit_to_colour[fruit]
    # If the colour is already a key in the accumulator, 
    # add colour: [fruit] as an entry.
    if not (colour in colour_to_fruit):
        colour_to_fruit[colour] = [fruit]
    # otherwise, append fruit to the existing list.
    else:
        colour_to_fruit[colour].append(fruit)


print(colour_to_fruit)
# -> {'orange': ['peach', 'orange'], 'purple': ['plum'], 'green': ['watermelon', 'pear'], 'yellow': ['banana'], 'red': ['cherry', 'pomegranate']}

print(colour_to_fruit['red'])
# -> ['pomegranate', 'cherry']

print(colour_to_fruit['red'][0])
# -> pomegranate


            #-----------------------Populating a Dictionary------------------------

import tkinter.filedialog
gradefile_name = tkinter.filedialog.askopenfilename()
gradefile = open(gradefile_name, 'r')

def read_grades(gradefile):
    '''(file open for reading) -> dict of {float:list of str}
     
    Read the grades from gradefile and return a dictionary where 
    each key is a grade and each value is the list of idsof students 
    who earned that grade.
     
    pre-condition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines
    contaning a student number and a grade.
    '''

    # Skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    # read the grade, accumulating them into a dict.
    grade_to_ids ={}     
    line = gradefile.readline()

    while line != '':
        student_id = line[:4]
        grade = float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
             grade_to_ids[grade].append([student_id])
        line = gradefile.readline()     
    print(grade_to_ids)    

read_grades(gradefile)


