# Import
try:
    from numpy import array, swapaxes, flipud, reshape
except ImportError:
    print('Install numpy for the Caesar Box cipher.')
from math import ceil
from random import choice
from string import ascii_letters as let, digits

# Zip all
def zipall(lists):
    '''Zips lists together with no values left out.'''
    maxLen = max([len(x) for x in lists])
    for x in lists:
        while len(x) < maxLen: x.append(None)
    return [y for x in list(zip(*lists)) for y in x if y != None]

# Encipher
def encipher_caesarbox(message, rows=3, nulls=False, keepNonLetNum=True):

    '''
    encipher_caesarbox(message, rows=3, nulls=False, keepNonLetNum=True)

    The message is written vertically and read horizontally.

    Arguments:
    message -- Message being enciphered
    rows -- Number of rows in the box, negative to start from the bottom
    nulls -- False to add nothing to the end of the message if it doesn't fit
             in the box, True to add random letters
    keepNonLetNum -- True to allow all characters in the message, False to
                     only allow letters and numbers

    Steps:
    1. If keepNonLetNum is False, non-letters/non-numbers in the message are
       removed.
    2. If the message length % rows is not 0, then blanks are added to the
       message, unless nulls is True, in which case random letters are added.
    3. The message is split into chunks, each the size of |rows|.
    4. Each chunk is put vertically into columns, top to bottom if rows is
       positive, but bottom to top if rows is negative.
       For example, if rows is 3 and the message is 'happy birthday' with
       keepNonLetNum as False and nulls as False, the box would look like:
       [h p i h y]
       [a y r d]
       [p b t a]
    5. The rows are read off from top to bottom as the cipher.
       In this example, the cipher is 'hpihyayrdpbta'.

    Returns the cipher and the box.
    '''

    ## Variables
    # General
    keepNonLetNum = bool(keepNonLetNum)
    ciphArray = []
    appended = ''
    # Message
    message = list(message)
    if not keepNonLetNum: message = [x for x in message if x in let + digits]
    # Rows
    rows = int(rows)
    neg = rows < 0
    if rows == 0: rows = 3
    rows = abs(rows)
    while len(message) % rows != 0:
        if nulls:
            x = choice(let)
            appended += x
            message.append(x)
        else:
            message.append('')

    ## Encipher
    # Lists
    message = [message[x:x + rows] for x in range(0, len(message), rows)]
    if neg: message = [list(reversed(x)) for x in message]
    # Array
    cipher = ''.join(zipall(message))
    ciphArray = message
    ciphArray = swapaxes(array(ciphArray), 0, 1)

    ## Return cipher and array
    return cipher, ciphArray

# Decipher
def decipher_caesarbox(cipher, rows):

    '''
    decipher_caesarbox(cipher, rows)

    The cipher is written horizontally and read vertically.

    Arguments:
    cipher -- Cipher being deciphered
    rows -- Number of rows in the box, negative to start from the bottom

    Steps:
    1. If the message length % rows is not 0, then blanks are added to the
       message.
    2. The length of the cipher / rows, rounded up is taken as columns and the
       remainder is taken as r.
       For example, if the cipher is 'hpihyayrdpbta' and rows is 3:
       a. The cipher length / rows = 13 / 3 = 4.333, rounded up = 5.
       b. The remainder = 3 - (rows * .333) = 2.
       c. Therefore, columns is 5 and r is 2.
    3. The message is split into chunks, each either the length of columns or
       columns - 1. For every amount in r, one chunk is interpreted to be
       the length of columns - 1.
       In this example, since r is 2 and rows is positive, 2 rows from the
       bottom of the box are length columns - 1.
       [1 2 3 4 5] (columns)
       [1 2 3 4]   (columns - 1)
       [1 2 3 4]   (columns - 1)
       Notice there are 2 short rows because r is 2.
       However, if rows is negative, the short rows start from the top, as:
       [1 2 3 4]
       [1 2 3 4]
       [1 2 3 4 5]
    4. The box is filled in with the letters from the cipher.
       In this example, the box is:
       [h p i h y]
       [a y r d]
       [p b t a]
    5. The cipher is read back into lists.
       In this exmple, the lists are [hap], [pyb], [irt], [hda], and [y].
    6. If rows is negative, each list is reversed.
    7. The lists are joined.
       In this example, the message is 'happybirthday'.

    Returns the message and the box.
    '''

    ## Variables
    # Cipher
    cipher = list(cipher)
    # Rows
    rows = int(rows)
    neg = rows < 0
    if rows == 0: rows = 3
    rows = abs(rows)
    columns = ceil(len(cipher) / rows)
    r = (rows - len(cipher) % rows) % rows
    # One column
    if columns == 1:
        if neg:
            while len(cipher) < rows: cipher.insert(0, '')
        else:
            while len(cipher) < rows: cipher.append('')
        ciphArray = reshape(array(cipher), (-1, 1))
        if neg: cipher = list(reversed(cipher))
        return ''.join(cipher), ciphArray

    ## Decipher
    # Negative rows
    if neg:
        cipher = [cipher[x:x + columns - 1] for x in
                  range(0, r * (columns - 1), columns - 1)] \
                 + [cipher[x:x + columns] for x in
                    range((columns - 1) * r, len(cipher), columns)]
    # Positive rows
    else:
        cipher = [cipher[x:x + columns] for x in
                  range(0, columns * (rows - r), columns)] \
                 + [cipher[x:x + columns - 1] for x in
                    range(columns * (rows - r), len(cipher), columns - 1)]
    for x in range(rows):
        if len(cipher[x]) < columns: cipher[x].append('')
    if neg: cipher = list(reversed(cipher))
    message = ''.join(zipall(cipher))
    ciphArray = array(cipher)
    if neg: ciphArray = flipud(ciphArray)

    ## Return message and array
    return message, ciphArray
