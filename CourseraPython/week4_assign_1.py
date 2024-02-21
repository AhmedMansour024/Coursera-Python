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

