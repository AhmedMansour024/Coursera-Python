def convert_to_minutes(num_hours):
    """(int) -> int

    Return the number of minutes there are in num_hours hours.
    
    >>> convert_to_minutes(2)
    120
    """
    result = num_hours * 60
    return result

def convert_to_seconds(num_hours):
    """(int) -> int

    Return the number of seconds there are in num_hours hours.
    
    >>> convert_to_seconds(2)
    7200
    """
    return convert_to_minutes(num_hours) * 60


def convert_kg_ib(kg):
    '''(number or float) -> float
       return the number of kg to pound
       >>>convert_kg_ib(100)
       220
       '''
    return kg*2.2


def convert_to_celsius(fahrenheit):
   ''' (number) -> float
   
   Return the number of Celsius degrees equivalent to fahrenheit degrees.
   
   >>> convert_to_ccelsius(32)
   0.0
   >>> convert_to_celsius(212)
   100.0
   '''
   temp = (fahrenheit - 32) * 5 / 9
   return temp


print(convert_to_celsius(212))


def count_vowels(word):
    # Convert the word to lowercase to handle both uppercase and lowercase vowels
    word = word.lower()
    
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Count the number of vowels in the word
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
            
    return count
