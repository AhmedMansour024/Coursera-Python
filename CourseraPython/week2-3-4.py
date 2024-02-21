def has_vowel(s):
    """(str) -> bool
    Return True if and only if s has at least one vowel, not including y.
    >>> has_vowel("Anniversary")
    True
    >>> has_vowel("xyz")
    False
    """
    vowel_found = False
    for char in s:
        if char in 'aeiouAEIOU':  
            vowel_found = True    

    return vowel_found



def collect_vowels(s):
    '''(str) -> int

    Return the  vowels in s. do not trwat the letter y as a vowel.

    >>>collect_vowels('Happy Anniversary!')
    'aAiea'
    >>>collect_vowels('xyz')
    ''
    '''
    
    vowels = ''

    for char in s:
        if not char in 'aeiouAEIOU':
            vowels = vowels + char
            
    return vowels

print(collect_vowels('Happy Anniversary!'))



def count_vowels(s):
    '''(str) -> int

    Return the number of vowels in s. do not treat the letter y as a vowel.

    >>>count_vowels('Happy Anniversary!')
    5
    >>>count_vowels('xyz')
    0
    '''
    num_vowels = 0

    for char in s:
        if not char in 'aeiouAEIOU ':
            num_vowels = num_vowels + 1
            
    return num_vowels

print(count_vowels('Happy Anniversary!'))




def inhospitable_weather(temp):
    ''' (number) -> bool
    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).
    >>> inhospitable_weather(20)
    False
    '''
    return 12 > temp or temp > 28


print(inhospitable_weather(15))



def report_status(scheduled_time, estimated_time):
    '''(number, number)-> str

    Return the flight status (on time, early, delayed) for a flight that was
    scheduled to arrive at scheduled_time, but is now estimated to arrive
    at estimated_time.

    >>> report_status(14.3, 14.3)
    'on_time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9.0, 9.5)
    'delayed'
    '''

    if scheduled_time== estimated_time:
        return 'on_time'
    elif scheduled_time>= estimated_time:
        return 'early'
    else:
        return 'delayed'




