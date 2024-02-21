# Select the expression(s) that evaluate to an int value.
# 8.0 % 4
8 + 3
8 % 6
# 7 + 8.5

           #----------------------------------------------

a = 7
b = a + 3    # 10
a = 9

           #----------------------------------------------

def f(x):
    y = x * 3
    return y - x

print(f(10))

           #----------------------------------------------

start = 'L'
middle = 8
end = 'R'

print(start + str(middle) + end)

               #--------------------------------------

def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.     
    Count how many times letter appears in s1 and in s2, 
    and return the bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))      # CODE MISSING HERE

print(count_max_letters('hello', 'world', 'l'))
print(count_max_letters('cat', 'abracadabra', 'a'))

               #--------------------------------------

def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''

    # if len(L1) == len(L2):
    #    return True
    # else:
    #    return False
    
    # or
    return len(L1) == len(L2)

print(same_length([0,1,2,3,4,9], [1,2,3,4,5]))

               #--------------------------------------

def burble(a, b):
    '''(int, float) -> str'''

def snorgle(L):
    '''(list of str) -> float
    Precondition: L has at least one element.'''



# burble([snorgle(1, 1.0), 'b'])
# burble(len(burble(1, 2.2)), 3.3)          # -> right
# snorgle([burble(1, 1.0), 'b'])            # -> right
# burble(snorgle(['a', 'b', 'c']), 8 // 3)

                   #--------------------------------------

def reverse(s):
    '''(str) -> str

    Return the reverse of s.

    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''

    result = ''
    i = len(s) - 1
    while i >= 0:
        result = result + s[i]
        i = i - 1   # CODE MISSING HERE

    return result 

print(reverse('abc'))
print(reverse('1234!'))

                   #--------------------------------------

def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''
  
    result = []
    for k in L:    # CODE MISSING HERE
        if k in d:
           result.append(k)

    return result

print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))

                   #--------------------------------------
# Q10: worng
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if len(d) == 1 and  k >= d[k] or len(d) > 1 and k <= d[k]:         # CODE MISSING HERE
             result = result + 1

    return result

print(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))
print(count_values_that_are_keys({1: 1}))
print(count_values_that_are_keys({1: 2}))


# def count_values_that_are_keys(d):
#     '''(dict) -> int

#     Return the number of values in d that are also keys in d.
   
#     >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
#     3
#     >>> count_values_that_are_keys({1: 1})
#     1
#     >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
#     2
#     >>> count_values_that_are_keys({1: 2})
#     0
#     '''

#     result = 0
#     for k in d:
#         if k in range(len(d)+1) and  k <= d[k]:         # CODE MISSING HERE
#              result = result + 1

#     return result

# print(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))
# print(count_values_that_are_keys({1: 1}))
# print(count_values_that_are_keys({1: 2}))

                   #--------------------------------------

def double_values(collection):
    for v in range(len(collection)):
         collection[v] = collection[v] * 2

L = [1, 2, 3]
double_values(L)
print(L)

d1 = {0: 10, 1: 20, 2: 30}
double_values(d1)
print(d1)

# s = '123'
# double_values(s)
# print(s)

# t = (1, 2, 3)
# double_values(t)

# d2 = {1: 10, 2: 20, 3: 30}
# double_values(d2)

                   #--------------------------------------

def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)

    return (neg, nonneg)

print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

def get_negative_nonnegative_lists(L):
    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] > 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])

    return (neg, nonneg)

print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

def get_negative_nonnegative_lists(L):
    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] < 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])

    return (neg, nonneg)

print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

def get_negative_nonnegative_lists(L):
    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] < 0:
                neg.append(L[row][col])

            nonneg.append(L[row][col])
    return (neg, nonneg)

print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

def get_negative_nonnegative_lists(L):
    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])
    return (neg, nonneg)

print(get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]))

                   #--------------------------------------
# Q13: worng
# def add_to_letter_counts(d, s):
#     '''(dict of {str: int}, str) -> NoneType

#     d is a dictionary where the keys are single-letter strings and the values
#     are counts.

#     For each letter in s, add to that letter's count in d.

#     Precondition: all the letters in s are keys in d.

#     >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
#     >>> add_to_letter_counts(letter_counts, 'eerie')
#     >>> letter_counts
#     {'i': 1, 'r': 6, 'e': 4}
#     '''

#     for c in s:
#         # CODE MISSING HERE
#         for k in d:
#             if c == k:
#                 d[k] = d[k] + 1
#     return d

# letter_counts = {'i': 0, 'r': 5, 'e': 1}
# add_to_letter_counts(letter_counts, 'eerie')
# print(letter_counts)


def add_to_letter_counts(d, s):
    for c in s:
        # CODE MISSING HERE
        d[c] = d.get(c, 0) + 1

    return d

letter_counts = {'i': 0, 'r': 5, 'e': 1}
add_to_letter_counts(letter_counts, 'eerie')
print(letter_counts)






