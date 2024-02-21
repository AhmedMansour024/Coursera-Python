def main():
    # user_input = input("emoji convertor: ")
    # x, y, z = input("calculator: pls type x + y: ").split()
    # s = calculator(x, y, z)
    # result = emoji_convertor(user_input)
    # print(s, result)
    return 0

def square_return(num):
    return ("the square of num is", num**2)

def emoji_convertor(input_str):
    # Replace :) with 🙂 and :( with 🙁
    emoji = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return emoji


def calculator(x, y, z):
    operator = y
    x = float(x)
    z = float(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z == 0:
            return ("Division by zero is not allowed.")
        result = x / z
    else:
        return ("Invalid operator. Please use +, -, *, or /.")
    return (result)


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


def inhospitable_weather(temp):
    ''' (number) -> bool
    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).
    >>> inhospitable_weather(20)
    False
    '''
    return 12 > temp or temp > 28


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


def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 thatappear at leastonce in s2. 
    The characters in the result will appear in the same order asthey appear in s1.

    >>> common_chars('abc', 'ad')
        'a'
    >>> common_chars('a', 'a')
        'a' 
    >>> common_chars('abb', 'ab')
        'abb' 
    >>> common_chars('abracadabra', 'ra')
        'araaara'
    '''
    
    ch = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    res = ''

    # BODY MISSING
    for ch in s1:
        if ch in s2:
            res = res + ch
            
    return res


def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    
    longer = int(len(dna1)) >= int(len(dna2))
    return longer


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid and contains no characters
    other than ('A', 'T', 'C' and 'G'). 

    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('ZXCV')
    False
    '''
    
##    valid = set('ATCG')
##    result = all(char in valid for char in dna)
##            
##    return result

##    or
    
    result = True
    for char in dna:
        if not (char in 'ATCG'):
            result = False
    return result


def insert_sequence(dna1,dna2,integer):
    '''(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('TACBACBACA','TACA',3)
    'TACTACABACBACA'
    '''
    
    insert = dna1[:integer] + dna2 + dna1[integer:]   
    return insert


def get_complement(dna):
    '''(str) -> str

    Return the nucleotide's complement ('A==T,C==G').

    >>>get_complement('T')
    'A'
    >>>get_complement('G')
    'C'
    '''
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complement_map.get(dna, False)


def get_complementary_sequence(dna):
    '''(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence. 
    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('GTCA')
    False
    '''
        
    dict_dna = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    cn = ''
    
    for dna in dna:
        if dna not in dict_dna:
            return False  # Return False if an invalid character is found
        cn += dict_dna[dna]  
    return cn

    
def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives
    a valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer


def up_to_vowel(word):
    ''' (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(word) and not (word[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + word[i]
        i = i + 1

    return before_vowel


# Q12:
def lines_startswith(file, letter):
     """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

     matches = []

     # CODE MISSING HERE
     matches.append(line.startswith(letter).rstrip('\n'))
 
     for line in file:    #right
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
            
     for line in file:    #wrong
        if letter in line:
            matches.append(line.rstrip('\n'))

     for line in file:    #right
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))       

     return matches

# answer
# file = open('testfile.txt', 'r')
# letter = 'a'
# lines_startswith(file, letter)
# ['abcde', 'aklmn', 'atuvw']

import ast

def count_docstring_lines(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
        tree = ast.parse(code)

        docstring_lines = [node.lineno for node in ast.walk(tree) if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str)]
        return len(docstring_lines)

# Replace 'your_file.py' with the path to your Python file
# file_path = 'Q12.py'
# lines_count = count_docstring_lines(file_path)
# print(f"Number of lines in docstrings: {lines_count}")




def count_docstring_lines(function):
    lines = function.__doc__.split('\n') if function.__doc__ else []
    return len([line for line in lines if line.strip()])



# Example usage:
lines_count = count_docstring_lines(lines_startswith)
print(f"Number of lines in docstring: {lines_count}")

def avr_grades_list(grades):
    '''([list]) -> number

    >>>avr_grades_list([30, 45, 60, 75, 70])
    total_avarage = 56.0
    failed_grade = (30, 45)
    '''
    passed_grades = [grade for grade in grades if grade >= 50]
    failed_grades = [grade for grade in grades if grade < 50]
    #print(passed_grades)
    #print(failed_grades)
    if len(passed_grades) >= len(failed_grades) and len(failed_grades) != 0:
        total_average = sum(passed_grades) / len(passed_grades)
        return f"Total average: {total_average:.2f}, Failed subjects: {failed_grades}"      
    elif len(passed_grades) <= len(failed_grades):
            return f"failed subject more then passed subject : {failed_grades}"
    elif len(failed_grades) == 0:
            total_average = sum(passed_grades) / len(passed_grades)
            return f"Total average: {total_average:.2f}, No failed subjects"
    else:
        return "Failed all subjects"

# Example usage:
grades_list = [75, 60, 90, 35, 80, 66, 55]
result = avr_grades_list(grades_list)
print(result)    #Total average: 67.50, Failed subjects: [40, 35, 25]


# Call main function
if __name__=="__main__":
    main()