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