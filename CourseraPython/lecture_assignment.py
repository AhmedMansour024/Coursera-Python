digits = '0123456789'
result = 100

for digit in digits:
    result = result - int(digit)

print(result)


digits = '0123456789'
result = 0

for digit in digits:
    result = digit

print(result)


digits = '0123456789'
result = ''

for digit in digits:
    result = result + digit * 2

print(result)


                ##########################################################

message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    new_message = new_message + char

print(new_message)


message = 'Happy 29th!'
new_message = ''

for char in message:
    if not char.isdigit():
        new_message = new_message + char
    else:
        new_message = new_message + str((int(char) + 1) % 10)

print(new_message)


message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char

print(new_message)


message = 'Happy 29th!'
new_message = ''

for char in message:
    new_message = new_message + str((int(char) + 1) % 10)

print(new_message)


              ###################################################################


int('3') in [len('a'), len('ab'), len('abc')]

len('mom') in [1, 2, 3]

len([1, 2, 3]) == len(['a', 'b', 'c'])

#     #####################################################

def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1
   
    print(result)

secret('abc123')

secret('abc')

secret('123abc')

#secret('123')    #<-<-<-<-<-<-<-<-<- error


def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    print(result)

mystery('abc123')

#mystery('abc')      #<-<-<-<-<-<-<-<-<- error

mystery('123abc')

mystery('123') 

           ##################################################

def example(L):
    """ (list) -> list
    Return a listcontaining every third item from L starting at index 0.
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    print(result)

L =[2,3,4,5,6,7,8,9]
example(L)


          ###############################################################################

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements from Lconcatenated together, starting with indices 0 and 1,2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        # MISSING CODE HERE
        i = i + 2
        
    print(compressed_list)


compress_list(['a', 'b', 'c', 'd'])

                #######################################################

#Define the range          <-<-<-<-<-<-<- EX Odd
start = 524
end = 10508
# Initialize variables
odd_sum = 0
number = start
# Loop while the number is within the range
while number <= end:
    if number % 2 != 0:
        odd_sum += number
    number += 1

print("The sum of odd numbers from", start, "through", end, "is:", odd_sum)   


# Define the range        <-<-<-<-<-<-<- EX Even
start = 524
end = 10508

# Initialize variables
even_sum = 0
number = start

# Loop while the number is within the range
while number <= end:
    if number % 2 == 0:
        even_sum += number
    number += 1

print("The sum of even numbers from", start, "through", end, "is:", even_sum)



#if using range:         <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<- EX Even
start = 524
end = 10508

# Initialize variables
even_sum = 0
number = start

# Loop while the number is within the range
while number <= end:
    if number % 2 == 0:
        even_sum += number
    number += 1

print("The sum of even numbers from", start, "through", end, "is:", even_sum)



#Define the range
start = 1523
end = 10503
# Initialize the sum
odd_sum = 0
# Loop through the range and add odd numbers to the sum
for number in range(start, end + 1):
    if number % 2 != 0:
        odd_sum += number

print("The sum of odd numbers from", start, "through", end, "is:", odd_sum)
    


    

                 #################################################

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total


def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1

    return total

L= [3 ,5 ,7 ,2]
print(for_version(L))
print(while_version(L))

                ##############################################



playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) >= 3:
         playlist.remove(song)

    while playlist.count(song) > 3:
         playlist.remove(song)

    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))


cap_song_repetition(playlist, 'Lola')

print(playlist)

             #############################################

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

#             ###########################################

values = []
for num in range(1, 4):       #<-<-<-<-<-<-<-
    values.append(num * 3)
print(values)

values = []
for num in range(1, 3):
    values.append(num * 3)
print(values)

values = []
for num in range(3, 9, 3):
    values.append(num)
print(values)

values = []
for num in range(3, 10, 3):     #<-<-<-<-<-<-<-
    values.append(num)
print(values)

            ##############################

for num in range(3,20,8):
    print(num)

for num in range(3,23,8):
    print(num)
        
for num in range(3,8,20):
    print(num)

for num in range(3,19,8):
    print(num)
        
