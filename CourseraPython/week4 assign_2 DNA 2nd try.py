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

    


