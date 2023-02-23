# Import
import random
import math
try:
    import numpy
except ImportError:
    print('Install numpy for the transposition ciphers.')
from string import ascii_lowercase as low, ascii_letters as let, digits

# Encipher
def encipher_columnartransposition(message, key, nulls=True,
                                   keepNonLetters=True):

    '''
    encipher_columnartransposition(message, key, nulls=True,
                                   keepNonLetters=True)

    The message is put into an array with the key as the row length and nulls
    or blanks in the empty spaces, and each column is sorted alphabetically
    according to the key, and read off in columns from left to right.

    Arguments:
    message -- Message being enciphered
    key -- Key that determines which order the columns are in when it is
           sorted, will only be letters and digits
    nulls -- True for random letters placed in empty spaces in the array,
             False for nothing put in the empty spaces
    keepNonLetters -- True to keep non-letters in the message, False to omit
                      non-letters

    Steps:
    1. Any non-letters/non-numbers are removed from the key, and if
       keepNonLetters is False, non-letters are removed from the message.
    2. If it's not already, characters are added to the message to make its
       length a multiple of the key length. If nulls is False, no characters
       are added.
    3. The message is put into an array with the key above it.
       For example, if the message is "happy birthday" with the key "cargo"
       with nulls as False and keepNonLetters as False, the array would be:
        c a r g o
       [h a p p y]
       [b i r t h]
       [d a y    ]
    4. Each column is rearranged in alphabetical order, with numbers first,
       then capital letters, then lowercase letters.
        a c g o r
       [a h p y p]
       [i b t h r]
       [a d     y]
    5. The columns are read off, top to bottom, from left to right.
       Example cipher: aiahbdptyhpry

    Returns the cipher.
    '''

    ## Variables
    # General
    cipher = ''
    message = list(message)
    array, columns = [], []
    nulls = bool(nulls)
    keepNonLetters = bool(keepNonLetters)
    # Revise message/key
    if not keepNonLetters: message = [x for x in message if x in let]
    key = [x for x in key if x in let + digits]
    while len(message) % len(key) != 0:
        message.append(('null', random.choice(low))[nulls])
    # Define key array
    for x in range(math.ceil(len(message) / len(key))):
        array.append(message[:len(key)])
        del message[:len(key)]
    array = numpy.asarray(array)
    # Sort columns
    for colNum, letter in enumerate(key):
        columns.append((letter, colNum, list(array[:,colNum])))
    columns = sorted(columns)

    ## Encipher
    for tup in columns:
        for value in tup[2]:
            if value != 'null': cipher += value

    ## Return cipher
    return cipher

