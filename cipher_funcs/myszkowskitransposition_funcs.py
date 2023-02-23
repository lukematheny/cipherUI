# Import
import random
import math
try:
    import numpy
except ImportError:
    pass
try:
    from caesarbox_funcs import zipall
except ModuleNotFoundError:
    from .caesarbox_funcs import zipall
from string import ascii_lowercase as low, ascii_uppercase as up, digits

# Encipher
def encipher_myszkowskitransposition(message, key, nulls=True,
                                     keepNonLetters=True):

    '''
    encipher_myszkowskitransposition(message, key, nulls=True,
                                     keepNonLetters=True)

    The message is put into an array with the key as the row length and nulls
    or blanks in the empty spaces, and each column is sorted alphabetically
    according to the key, and read off in columns from left to right but in
    rows for only the columns that have the same key letter.

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
       For example, if the message is "happy birthday" with the key "tomato"
       with nulls as False and keepNonLetters as False, the array would be:
        t o m a t o
       [h a p p y b]
       [i r t h d a]
       [y          ]
    4. Each column is rearranged in alphabetical order, with numbers first,
       then capital letters, then lowercase letters.
        a m o o t t
       [p p a b h y]
       [h t r a i d]
       [        y  ]
    5. Any repeating letters are zipped together into one column.
        a m o t
       [p p a h]
       [h t b y]
       [    r i]
       [    a d]
       [      y]
    6. The columns are read off, top to bottom, from left to right.
       Example cipher: phptabrahyidy

    Returns the cipher.
    '''

    ## Variables
    # General
    cipher = ''
    message = list(message)
    nulls = bool(nulls)
    keepNonLetters = bool(keepNonLetters)
    # Revise message/key
    if not keepNonLetters: message = [x for x in message if x in low + up]
    key = [x for x in key if x in low + up + digits]
    while len(message) % len(key) != 0:
        message.append(('null', random.choice(low))[nulls])
    # Define array
    array = []
    for x in range(math.ceil(len(message) / len(key))):
        array.append(message[:len(key)])
        del message[:len(key)]
    array = numpy.asarray(array)
    # First sorting of columns
    columns = []
    for colNum, letter in enumerate(key):
        columns.append((letter, colNum, list(array[:,colNum])))
    columns = sorted(columns)
    # Document letters
    letters = []
    for tup in columns: letters.append(tup[0])
    # Second sorting of columns
    zColumns = []
    for letter, number, column in columns:
        if len([x for x in letters if x == letter]) > 1:
            indices = [x for x, y in enumerate(letters) if y == letter]
            column = zipall([columns[x][2] for x in indices])
        zColumns.append((letter, column))
    # Remove duplicates
    letters, columns = [], []
    for ind, tup in enumerate(zColumns):
        if tup[0] in letters: columns.append(ind)
        else: letters.append(tup[0])
    for ind in reversed(columns): del zColumns[ind]

    ## Encipher
    for letter, column in zColumns:
        for value in column:
            if value != 'null': cipher += value

    ## Return cipher
    return cipher
