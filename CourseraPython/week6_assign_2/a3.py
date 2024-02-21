"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
       
    return word in wordlist
            
#print(is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'SOB'))

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    str_row = ''
    if len(board) > row_index:
        list_row = board[row_index]
        for char in list_row:
            str_row = str_row + char
    else:
        str_row = 'Wrong row_index'     

    return str_row

#print(make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    str_column = ''
    if len(board[0]) > column_index:
        for list in board:
            str_column = str_column + list[column_index]
    else:
        str_column = 'Wrong column_index'    

    return str_column
        
#print(make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2))       


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    
    return False

#print(board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB'))


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            return True

    return False    

#print(board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO'))

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            return True

    return False

#print(board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT'))


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    score = 0
    if len(word) < 3:
        score = score + len(word) * 0
    elif len(word) >= 3 and len(word) <= 6:
        score = score + len(word) * 1
    elif len(word) >= 7 and len(word) <= 9:
        score = score + len(word) * 2
    else:
        score = score + len(word) * 3

    return score


#print(word_score('DR'))

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    new_score = word_score(word)
    if new_score != 0:
        player_info[1] = player_info[1] + word_score(word) 
        return player_info

#print(update_score(['Jonathan', 4], 'ANT'))

def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    num_words = 0

    for word in words:        
        for row_index in range(len(board)):
            if word in make_str_from_row(board, row_index):
                num_words = num_words + 1
        for column_index in range(len(board[0])):
            if word in make_str_from_column(board, column_index):                
                num_words = num_words + 1
    return num_words            

              
#print(num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'XS', 'SOB', 'TO']))       


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words_file_list = [line.strip() for line in words_file.readlines()]
    return words_file_list
       


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    board_file_list = [line.strip() for line in board_file.readlines()]
    return board_file_list