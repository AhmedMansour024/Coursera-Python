# d = {'a': 1, 'b': 2}
# # CODE MISSING HERE
# d['c'] = 3
# print(d)
# # {'a': 1, 'c': 3, 'b': 2}

           #----------------------------------------------

# d = {'a': 1, 'b': 2}
# # CODE MISSING HERE
# d['b'] = 3
# print(d)
# # {'a': 1, 'b': 3}

           #----------------------------------------------

# d = {'a': [1, 3], 'b': [5, 7]}
# # CODE MISSING HERE
# # d['a'].append(2)
# # d['a'].sort()
# # or
# d['a'].insert(1, 2)
# print(d)
# # {'a': [1, 2, 3], 'b': [5, 7]}

           #----------------------------------------------

# d = {'a': 1, 'c': 3, 'b': 2}
# # 2 in d
# "b" in d
# # 'B' in d
# not ('e' in d)

           #----------------------------------------------

# d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}
# len(d['b'])
# # len(d['a' + 'c'])
# len(d['a']) + len(d['c'])
# # len(d['a'])

           #----------------------------------------------

# tup = (1, 2, 3)
# # # subtup = tup[0:2]
# # tup[-2] = 4
# # tup.reverse()
# # # tup[0:2] == (10, 30)

           #----------------------------------------------

# # Select the expression(s) that can be used as dictionary keys.
# (1, 'fred', 2.0)
# # ['a', 'b']
# # {1: 2, 3: 4}
# ('single',)

           #----------------------------------------------

d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
total = 0
for k in d:
    total = total + k
print(total)

d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
L = []
for k in d:
    L.append(k)

total = len(L)
print(total)

d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
L = []
for k in d:
    L.extend(d[k])

total = len(L)
print(total)

d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
total = 0
for k in d:
    total = total + len(d[k])
print(total)

           #----------------------------------------------

{1: 10, 1: 20, 1: 30}      # -> {1: 30}

           #----------------------------------------------

L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
   d[item[0]] = item[1]

print(d)

           #----------------------------------------------

def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of     that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate

print(eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1}))
print(eat({'apple': 0, 'banana': 0}))

# Try to eat one of each fruit: reduce by 1 all quantities greater than 0 associated with each fruit in 
# d and return True if and only if any fruit was eaten.

           #----------------------------------------------

def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # # CODE MISSING HERE
    # for k in d:
    #     for i in range(len(d[k])):
    #         found = (d[k][i] == v)
    
    # for k in d:
    #     if v == k:
    #         found = True
    
    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True
    for k in d:
        if v in d[k]:
            found = True
    
    return found

print(contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]}))
print(contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}))