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

#print(up_to_vowel('hello'))

print(get_answer('do you like python ?'))