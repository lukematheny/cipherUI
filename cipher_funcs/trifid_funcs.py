# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
try:
    import numpy
except ImportError:
    print('Install numpy for Trifid cipher display.')
    numpy = None
from string import ascii_lowercase as low, ascii_letters as let

# Encipher
def encipher_trifid(message, playfairKey=None, size=5):

    '''
    encipher_trifid(message, playfairKey=None, size=5)

    Coordinates are retrieved from a grid, rearranged, then translated.

    Arguments:
    message -- Message being enciphered, should have letters and/or +
    playfairKey -- Playfair key for 3x3x3 grid, including letters and +
    size -- Size of each grouping of letters for how they are read off

    Steps:
    1. The Playfair key is put through the playfair_square function with the
       alphabet as the letters and a plus sign. This gives 27 characters,
       which are used to create a 3x3x3 grid.
       For example, if the Playfair key is "example", the grid is:
          Box 1      Box 2      Box 3
       [[[e x a]   [[f g h]   [[r s t]
         [m p l]    [i j k]    [u v w]
         [b c d]],  [n o q]],  [y z +]]]
    2. The message is written out, grouped into sizes based on the size
       argument.
       With the message "hello" and a size of 2, the message is "he ll o".
    3. Every letter in the message is translated to coordinates, with the box
       number, then the row number, then the column number.
       In this example, the numbers are:
       h e   l l   o
       2 1   1 1   2
       1 1   2 2   3
       3 1   3 3   2
    4. The numbers are read off horizontally in their own groups and grouped
       into 3s. The cipher numbers here are 211 131 (first group), 112 233
       (second group), and 232 (last group).
    5. The resulting numbers are translated back into letters, in the same
       pattern as step 3.
       Cipher: fbxqo

    Returns the cipher and the 3x3x3 grid.
    '''

    ## Variables
    # General
    coords, cipher = [], ''
    message = [x.lower() for x in message if x in let + '+']
    size = abs(round(size))
    # Playfair key and square
    playfairKey = playfair_square(playfairKey, False, True, low + '+')
    key = [playfairKey[x:x + 3] for x in range(0, 27, 3)]
    key = [key[x:x + 3] for x in range(0, 9, 3)]
    if numpy: playfairKeyGrid = numpy.array(key)
    else: playfairKeyGrid = None
    playfairKey = ''.join(playfairKey)

    ## Encipher
    # Coordinates
    for letter in message:
        for fInd, first in enumerate(key):
            for sInd, second in enumerate(first):
                for tInd, third in enumerate(second):
                    if letter == third:
                        coords.append((fInd, sInd, tInd))
                        break
    coords = [coords[x:x + size] for x in range(0, len(coords), size)]
    coords = [list(zip(*x)) for x in coords]
    coords = [[z for y in x for z in y] for x in coords]
    coords = [[x[y:y + 3] for y in range(0, len(x), 3)] for x in coords]
    coords = [y for x in coords for y in x]
    # Retrieve letters
    for x, y, z in coords:
        cipher += key[x][y][z]

    ## Return cipher, key, & grid
    return cipher, playfairKey, playfairKeyGrid

# Decipher
def decipher_trifid(cipher, playfairKey, size):

    '''
    decipher_trifid(cipher, playfairKey, size)

    Coordinates are retrieved from a grid, rearranged, then translated.

    Arguments:
    cipher -- Cipher being deciphered, should have letters and/or +
    playfairKey -- Playfair key for 3x3x3 grid, including letters and +
    size -- Size of each grouping of letters for how they are read off

    Steps:
    1. The Playfair key is put through the playfair_square function with the
       alphabet as the letters and a plus sign. This gives 27 characters,
       which are used to create a 3x3x3 grid.
       For example, if the Playfair key is "example", the grid is:
          Box 1      Box 2      Box 3
       [[[e x a]   [[f g h]   [[r s t]
         [m p l]    [i j k]    [u v w]
         [b c d]],  [n o q]],  [y z +]]]
    2. The cipher is written out, grouped into sizes based on the size
       argument.
       With the cipher "fbxqo" and a size of 2, the cipher is "fb xq o".
    3. Every letter in the cipher is translated to coordinates, with the box
       number, then the row number, then the column number.
       In this example, the numbers are:
       f     b       x     q       o
       2 1 1 1 3 1   1 1 2 2 3 3   2 3 2
    4. The coordinates are put into lists, in respect to each group.
       E.g: [[2,1,1,1,3,1], [1,1,2,2,3,3], [2,3,2]]
    5. Each coordinate sublist is reorganized into tuples, their size being
       the length of their group.
       E.g: [[(2,1),(1,1),(3,1)], [(1,1),(2,2),(3,3)], [(2),(3),(2)]]
                 2 letters             2 letters         1 letter
    6. Each sublist is zipped together.
       E.g: │ [(2, 1) [(1, 1) [(2)
            │  (1, 1)  (2, 2)  (3)
            ▼  (3, 1)] (3, 3)] (2)]
              [213 111 123 123 232]
    7. The resulting numbers are translated back into letters, in the same
       pattern as step 3.
       Message: hello

    Returns the message and the 3x3x3 grid.
    '''

    ## Variables
    coords, message = [], ''
    cipher = [x.lower() for x in cipher if x in let + '+']
    size = round(size)
    # Playfair key and square
    playfairKey = playfair_square(playfairKey, False, True, low + '+')
    key = [playfairKey[x:x + 3] for x in range(0, 27, 3)]
    key = [key[x:x + 3] for x in range(0, 9, 3)]
    if numpy: playfairKeyGrid = numpy.array(key)
    else: playfairKeyGrid = None
    playfairKey = ''.join(playfairKey)

    ## Encipher
    # Coordinates
    for letter in cipher:
        for fInd, first in enumerate(key):
            for sInd, second in enumerate(first):
                for tInd, third in enumerate(second):
                    if letter == third:
                        coords.append((fInd, sInd, tInd))
                        break
    coords = [coords[x:x + size] for x in range(0, len(coords), size)]
    coords = [[z for y in x for z in y] for x in coords]
    coords = [[x[y:y + len(x) // 3] for y in
               range(0, len(x), len(x) // 3)] for x in coords]
    coords = [list(zip(*x)) for x in coords]
    coords = [z for x in coords for y in x for z in y]
    coords = [coords[x:x + 3] for x in range(0, len(coords), 3)]
    # Retrieve letters
    for x, y, z in coords:
        message += key[x][y][z]

    ## Return message, key, & grid
    return message, playfairKey, playfairKeyGrid
