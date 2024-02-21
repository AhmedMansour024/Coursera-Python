
text = "Hello, how are you?"

# Split the string based on spaces
words = text.split()

print(words)  # Output: ['Hello,', 'how', 'are', 'you?']

                #--------------------------------------

text = "   Hello, World!   "

# Remove leading and trailing whitespace
clean_text = text.strip()

print(f'Original: "{text}"')
print(f'Cleaned: "{clean_text}"')

                #---------------------------------

words = ['Hello,', 'how', 'are', 'you?']

# Join the list elements into a single string using spaces
text = ' '.join(words)

print(text)  # Output: 'Hello, how are you?'

                #----------------------------------

name = "Alice"
age = 30

# Using an f-string to create a formatted string
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)

                #-------------------------------

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
    #CODE MISSING HERE
    #inner_list = []

    for i in range(len(list1)):              #<-----
        pairs.append([list1[i], list2[i]])


    # inner_list = []
    # for i in range(len(list1)):
    #     inner_list.append(list1[i])
    #     inner_list.append(list2[i])
    #     pairs.append(inner_list)
    
    # for i in range(len(list1)):
    #     inner_list = []
    #     inner_list.append(list1[i])
    #     inner_list.append(list2[i])
    # pairs.append(inner_list)

#     for i in range(len(list1)):            #<----
#         inner_list = []
#         inner_list.append(list1[i])
#         inner_list.append(list2[i])
#         pairs.append(inner_list)

    return pairs

print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))

                #-----------------------------------
from "/Coursera Python\week6 assign_2\a3.py" import make_str_from_row


def make_list_from_rows(board):
    """ (list of list of str) -> list of str

    Return a list containing all the characters from each row of the board
    concatenated as individual strings.

    """
    list_from_rows = []
    for row_index in range(len(board)):
        str_from_row = make_str_from_row(board, row_index)
        list_from_rows.append(str_from_row)

    return list_from_rows

# Example usage:
board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
result = make_list_from_rows(board)
print(result)  # Output will be ['ANTT', 'XSOB']


                 #----------------------------------

file_name = '\Users\nabil\Documents\week6 assign_2' 
words_list = [line.strip() for line in file_name.readlines()]   # to convert a file to a list without '\n'


               #--------------------------------------

my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 'inserted')
print(my_list)                 # [1, 2, 'inserted', 3, 4, 5]

my_list = [1, 2, 3]
another_list = [4, 5, 6]

my_list.extend(another_list)
print(my_list)                  # [1, 2, 3, 4, 5, 6]

               #--------------------------------------

start = 'L'
middle = 8
end = 'R'

print(start + str(middle) + end)  # ->'L8R'

               #--------------------------------------
# dict.get(key, 0)    # get the value of that key

def add_to_letter_counts(d, s):
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

letter_counts = {'i': 0, 'r': 5, 'e': 1}
add_to_letter_counts(letter_counts, 'eerie')
print(letter_counts)  # Output: {'i': 1, 'r': 6, 'e': 4}

               #------------------------------------

bob , kimy, temy = 16, 15, 21





