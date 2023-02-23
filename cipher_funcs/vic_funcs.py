# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
try:
    import numpy
except ImportError:
    print('Install numpy for the VIC Cipher.')
from random import choice
from string import ascii_lowercase as low, digits

# Encipher
def encipher_vic(message, addKey=None, numKey=None, numExclude=None,
                 row1key=None, remainKey=None, decipher=False):

    '''
    encipher_vic(message, addKey=None, numKey=None, numExclude=None,
                 row1key=None, remainKey=None, decipher=False)

    The message is put through a grid, turned into coordinates, added with a
    key, then a cipher is taken from the new coordinates.

    Arguments:
    message -- Message being enciphered
    addKey -- Numbers to be added to coordinates during encryption
    numKey -- Playfair key (digits) for horizontal coordinates
    numExclude -- The two coordinate numbers to exclude from the top row and
                  to be used for vertical coordinates
    row1key -- Playfair key for the top row in the grid, letters in 'restonia'
    remainKey -- Playfair key for the rest of the grid, letters in the
                 alphabet excluding letters in 'restonia', including / and .
    decipher -- False to encipher, True to decipher with message as the cipher

    Steps:
    1. The grid is made.
       a. The numKey Playfair sequence is at the top and the 2 numExclude
          numbers are on the side. With the numKey as 0123456789 and
          numExclude as 26, the grid is:
          [  0 1 2 3 4 5 6 7 8 9]
          [                     ]
          [2                    ]
          [6                    ]
       b. The row1key Playfair sequence is put on the top row, skipping the
          numbers in numExclude. The remainKey Playfair sequence fills in the
          rest of the grid. With row1key as 'etaonris' and remainKey as
          'bcdfghjklmpq/uvwxyz.', the grid is:
          [  0 1 2 3 4 5 6 7 8 9]
          [  e t   a o n   r i s]
          [2 b c d f g h j k l m]
          [6 p q / u v w x y z .]
    2. The message is converted to coordinates with the grid.
       If the message is 'Mary, Queen of Scots', the coordinates are:
        m a r  y  q  u e e n o  f s  c o t s
       29 3 7 67 61 63 0 0 5 4 23 9 21 4 1 9
    3. The addKey is repeated to fit the length of the coordinates. If
       decipher is False, they are added together. If decipher is True, the
       addKey is subtracted from the coordinates. Each individual number is
       added/subrtacted, so modular addition is used for each value.
       This is their addition in this example with addKey as 1542:
         2 9 3 7 6 7 6 1 6 3 0 0 5 4 2 3 9 2 1 4 1 9
       + 1 5 4 2 1 5 4 2 1 5 4 2 1 5 4 2 1 5 4 2 1 5
       = 314 7 9 71210 3 7 8 4 2 6 9 6 510 7 5 6 214
       The numbers are made modulo to 10 (ten is added/subtracted until the
       number is in the 0-9 range)
       = 3 4 7 9 7 2 0 3 7 8 4 2 6 9 6 5 0 7 5 6 2 4
    4. The numbers are paired based on if the first number is in numExclude.
       If the last number is in numExclude, the first number is added to the
       end and paired with it (this may add an extra letter when deciphering)
       E.g: 3 4 7 9 7 20 3 7 8 4 26 9 65 0 7 5 62 4
    5. Each letter for the cipher is retrieved from the grid from the numbers.
       E.g: The cipher is 'aorsrbariojswern/o'.

    Returns the cipher and grid.
    '''

    ## Variables
    # General
    cipher, coords = '', []
    decipher = bool(decipher)
    message = [x for x in message.lower() if x in low + '/.']
    # Add key
    if addKey == None: addKey = '0123456789'
    elif isinstance(addKey, float): addKey = str(int(addKey))
    elif isinstance(addKey, int): addKey = str(addKey)
    elif addKey.isalpha(): addKey = [low.index(x) for x in addKey.lower()]
    elif not addKey.isdigit(): addKey = '0123456789'
    # Excluded numbers
    if numExclude != None:
        if isinstance(numExclude, float): numExclude = int(numExclude)
        if isinstance(numExclude, int): numExclude = str(numExclude)
        if numExclude.isdigit():
            numExclude = [x for x in numExclude if x in digits]
            numExclude = sorted(set(numExclude), key=numExclude.index)
            numExclude = ''.join(numExclude[:2])
        else:
            numExclude = ''.join(x for x in numExclude if x in digits)
        while len(numExclude) < 2:
            numExclude += choice(digits.replace(numExclude, ''))
    else:
        numExclude = choice(digits)
        numExclude += choice(digits.replace(numExclude, ''))
    numExclude = ''.join(sorted(numExclude))
    # Playfair keys
    if numKey != None: numKey = str(numKey)
    numKey = playfair_square(numKey, alphabet=digits)
    row1key = playfair_square(row1key, alphabet='restonia')
    remainKey = playfair_square(remainKey, 0, 1, 'bcdfghjklmpquvwxyz/.')
    # Dicts
    excDict = dict(zip('012', '0' + numExclude))
    excDictR = dict(zip(numExclude, '12'))
    numDict = dict(zip(digits, numKey))
    numDictR = dict(zip(numKey, digits))
    # Array
    exc = sorted(numDictR[numExclude[0]] + numDictR[numExclude[1]])
    row1key.insert(int(exc[0]), ' ')
    row1key.insert(int(exc[1]), ' ')
    grid = numpy.array([row1key, remainKey[:10], remainKey[10:]])

    ## Encipher
    # Coordinates
    for letter in message:
        i = numpy.where(grid==letter)
        x, y = excDict[str(i[0][0])], numDict[str(i[1][0])]
        if x != '0': coords.append(x)
        coords.append(y)
    # Add/subtract
    while len(addKey) < len(coords): addKey += addKey
    for (cInd, coord), add in zip(enumerate(coords), addKey):
        x = (int(coord) + int(add), int(coord) - int(add))[decipher]
        coords[cInd] = str(x % 10)
    # Reformat
    for xInd, x in enumerate(coords):
        if x in numExclude:
            try:
                coords[xInd] = x + coords[xInd + 1]
                del coords[xInd + 1]
            except IndexError:
                coords[xInd] = x + coords[0]
    for xInd, x in enumerate(coords):
        if len(x) == 2: coords[xInd] = excDictR[x[0]] + numDictR[x[1]]
        else: coords[xInd] = '0' + numDictR[x[0]]
    # Retrieve letters
    for x in coords:
        cipher += grid[int(x[0]), int(x[1])]
    # Reformat grid
    grid = grid.tolist()
    grid[0].insert(0, ' ')
    grid[1].insert(0, numExclude[0])
    grid[2].insert(0, numExclude[1])
    grid.insert(0, list(' ' + ''.join(numKey)))
    grid = numpy.array(grid)

    ## Return cipher and grid
    return cipher, grid

# Decipher
def decipher_vic(cipher, subtractKey, numKey, numExclude, row1key, remainKey):

    '''
    decipher_vic(cipher, subtractKey, numKey, numExclude, row1key, remainKey)

    The cipher is put through a grid, turned into coordinates, subtracted with
    a key, then a message is taken from the new coordinates.

    Arguments:
    cipher -- Cipher being deciphered
    subtractKey -- Numbers to be subtracted from coordinates during decryption
    numKey -- Playfair key (digits) for horizontal coordinates
    numExclude -- The two coordinate numbers to exclude from the top row and
                  to be used for vertical coordinates
    row1key -- Playfair key for the top row in the grid, letters in 'restonia'
    remainKey -- Playfair key for the rest of the grid, letters in the
                 alphabet excluding letters in 'restonia', including / and .

    Steps:
    1. The message and grid are taken from the encipher_vic function with
       cipher as the message, subtractKey as the addKey, and decipher as True.

    Returns the message and grid.
    '''

    ## Decipher
    message, grid = encipher_vic(cipher, subtractKey, numKey, numExclude,
                                 row1key, remainKey, True)

    ## Return message and grid
    return message, grid
