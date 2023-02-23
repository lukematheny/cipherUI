# Import
try:
    import numpy as np
except ImportError:
    print('Install numpy for the route cipher.')
from math import sqrt, ceil
from random import choice
from string import ascii_letters as let, digits, ascii_lowercase as low, \
                   ascii_uppercase as up

# Create dimension
def create_dim(dimension, message, rev=False):
    '''Row or column created from the original dimension and the message.'''
    dimension = list(dimension)  # Array to list
    if rev: dimension = list(reversed(dimension))  # Reverse
    for ind, x in enumerate(dimension):  # Fill in dimension where 0s are
        if x == 0: dimension[ind] = message[0]; del message[0]
    if rev: dimension = list(reversed(dimension))  # Reverse to normal
    return dimension, message

# Encipher
def encipher_route(message, write='random', read='random',
                   rows=None, keepNonLetNum=True, appendage='let'):

    '''
    encipher_route(message, write='random', read='random',
                   rows=None, keepNonLetNum=True, appendage='let')

    Arguments:
    message -- Message being enciphered
    write -- How the message is written into its grid, refer to syntax
    read -- How the cipher is read from the grid, refer to syntax
    rows -- How many rows are in the grid. If None or 0, defaults to the
            square root of the message length, divided by 1.5, rounded to the
            nearest number [round(sqrt(len(message)) / 1.5)]
    keepNonLetNum -- True to allow all characters, False to only allow
                     letters and numbers
    appendage -- A string used to signify what will be added to the message if
                 its length doesn't line up with the row argument, can be low
                 [lowercase letters], up [uppercase letters], let [all
                 letters], digits [numbers], low + digits [lowercase letters
                 and numbers], up + digits [uppercase letters and numbers], or
                 let + digits [all letters and numbers]

    Syntax for write and read:
    -Sample grid:
     [[0, 1, 2, 3],
      [4, 5, 6, 7],
      [8, 9, x, y]]
    -Three arguments in a string separated by semicolons [;]
     1. Pattern (Samples assume h and tl):
        z -- Goes from each row to the beginning of the next
             Sample is read '0 1 2 3 4 5 6 7 8 9 x y'.
        s -- Beginning of each row connects to the end of the previous
             Sample is read '0 1 2 3 7 6 5 4 8 9 x y'.
        sp -- Spiral inward
              Sample is read '0 1 2 3 7 y x 9 8 4 5 6'.
     2. Starting direction (Samples assume z and tl):
        h -- Horizontal
             Sample is read '0 1 2 3 4 5 6 7 8 9 x y'.
        v -- Vertical
             Sample is read '0 4 8 1 5 9 2 6 x 3 7 y'.
     3. Starting point (Samples assume z and h):
        tl -- Top left
              Sample is read '0 1 2 3 4 5 6 7 8 9 x y'.
        tr -- Top right
              Sample is read '3 2 1 0 7 6 5 4 y x 9 8'.
        bl -- Bottom left
              Sample is read '8 9 x y 4 5 6 7 0 1 2 3'.
        br -- Bottom right
              Sample is read 'y x 9 8 7 6 5 4 3 2 1 0'.
    -Examples:
     1. 'z;v;bl'
     2. 'sp;v;br'
     3. 's;h;tl'
     4. 'sp;h;tr'
    -Not case sensitive but must be separated by semicolons.
    -Equal the argument to None, 'r', 'rand', or 'random' for a random
     read or write combination.

    Steps:
    1. If row, read or write is random or None, they are auto-generated.
    2. Message is lengthened if needed, according to the argument appendage.
    3. Message is written into a grid by the arguments write and rows.
    4. Cipher is read from the grid by the argument read.

    Returns the cipher, the cipher grid, and write, read, & appended letters
    in case they were needed or not specified.
    '''

    ## Variables
    # General
    cipher = []
    keepNonLetNum = bool(keepNonLetNum)
    cRand = [None, 'r', 'rand', 'random']
    # Message & rows
    message = list(message)
    if not keepNonLetNum: message = [x for x in message if x in let + digits]
    if rows in [None, 0]: rows = round(sqrt(len(message)) / 1.5)
    rows = int(abs(rows))
    columns = ceil(len(message) / rows)
    appended = ''
    while len(message) % rows != 0:
        x = choice(eval(appendage))
        appended += x
        message.append(x)
    message = [ord(x) for x in message]  # Because numpy hates strings
    # Write/read
    if write != None: write = write.lower()
    if read != None: read = read.lower()
    if write in cRand:
        write = ';'.join((choice(['s', 'z', 'sp']),
                          choice(['v', 'h']),
                          choice(['tl', 'tr', 'bl', 'br'])))
    if read in cRand:
        read = ';'.join((choice(['s', 'z', 'sp']),
                         choice(['v', 'h']),
                         choice(['tl', 'tr', 'bl', 'br'])))
    write, read = write.split(';'), read.split(';')

    ## Encipher
    # Write
    if write[1] == 'v': rows, columns = columns, rows  # We'll swap axes later
    if write[0] == 'sp':  # Spiral
        temp, t = np.zeros((rows, columns)), 0
        while len(message) != 0:
            temp[t], message = create_dim(temp[t], message)  # Top
            if len(message) == 0: break
            temp[:,-t-1], message = create_dim(temp[:,-t-1], message)  # Right
            if len(message) == 0: break
            temp[-t-1], message = create_dim(temp[-t-1], message, 1)  # Bottom
            if len(message) == 0: break
            temp[:,t], message = create_dim(temp[:,t], message, 1)  # Left
            t += 1
        message = temp
    else:
        message = [list(message[x:x + columns])
                   for x in range(0, len(message), columns)]
        if write[0] == 's':  # Set every odd numbered row backwards
            for ind, x in enumerate(message):
                if ind % 2 != 0: message[ind] = message[ind][::-1]
        message = np.array(message)
    if write[1] == 'v':
        rows, columns = columns, rows  # Reset rows & columns
        message = np.swapaxes(message, 0, 1)  # Swap axes
    if write[2][0] == 'b': message = np.flipud(message)  # Flip down
    if write[2][1] == 'r': message = np.fliplr(message)  # Flip right
    cipher = message
    message = np.vectorize(int)(message)
    message = np.vectorize(chr)(message)
    # Read
    if read[2][1] == 'r': cipher = np.fliplr(cipher)  # Flip left
    if read[2][0] == 'b': cipher = np.flipud(cipher)  # Flip up
    if read[1] == 'v': cipher = np.swapaxes(cipher, 0, 1)  # Swap axes
    if read[0] == 's':  # Set every odd numbered row backwards
        for ind, x in enumerate(cipher):
            if ind % 2 != 0: cipher[ind] = cipher[ind][::-1]
    elif read[0] == 'sp':  # Spiral
        temp = []
        while np.size(cipher) != 0:
            temp.append(list(cipher[0]))  # Top
            cipher = np.delete(cipher, 0, 0)
            if np.size(cipher) == 0: break
            temp.append(list(cipher[:,-1]))  # Right
            cipher = np.delete(cipher, -1, 1)
            if np.size(cipher) == 0: break
            temp.append(list(reversed(cipher[-1])))  # Bottom
            cipher = np.delete(cipher, -1, 0)
            if np.size(cipher) == 0: break
            temp.append(list(reversed(cipher[:,0])))  # Left
            cipher = np.delete(cipher, 0, 1)
        cipher = temp
    # Revise variables
    cipher = ''.join(chr(int(y)) for x in cipher for y in x)
    write, read = ';'.join(write), ';'.join(read)

    ## Return cipher, message, write, read, and appended
    return cipher, message, write, read, appended

# Decipher
def decipher_route(cipher, write, read, rows):

    '''
    decipher_route(cipher, write, read, rows)

    Arguments:
    cipher -- Cipher being deciphered
    write -- How the message was written when it was enciphered (refer to
             encipher_route)
    read -- How the message was read when it was enciphered (refer to
            encipher_route)
    rows -- Number of rows in the message grid

    Steps:
    1. The arguments are put through encipher_route with read and write
       switched as in encipher_route(cipher, read, write, rows).

    Returns the message and cipher grid.
    '''

    ## Decipher
    message, cipher, a, b, c = encipher_route(cipher, read, write, rows)

    ## Return message & cipher
    return message, cipher
