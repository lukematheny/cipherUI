# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
try:
    import numpy
except ImportError:
    print('Install numpy for the four-square cipher.')
from string import ascii_uppercase as up, digits

# Encipher
def encipher_foursquare(message, trPlayfairKey=None, 
                        blPlayfairKey=None, numbers=False):
    
    '''
    encipher_foursquare(message, trPlayfairKey=None,
                        blPlayfairKey=None, numbers=False)
    
    Four Playfair squares are generated and put in a 2x2 grid. Each pair of
    message letters are translated to different pairs using the rows and
    columns of each letter.
    
    Arguments:
    message -- Message being enciphered, if its length is odd, the last letter
               is repeated
    trPlayfairKey -- Top right Playfair square key
    blPlayfairKey -- Bottom left Playfair square key
    numbers -- False for the squares to be 5x5 without j, True for the squares
               to be 6x6 with numbers
    
    Steps:
    1. Two Playfair squares are generated from the arguments trPlayfairKey, 
       blPlayfairKey, and numbers with the function playfair_square.
    2. The trPlayfairKey square is put in the top right, the blPlayfairKey
       square is put in the bottom left, with 2 normal alphabets in the other
       places. For example, with both Playfair keys as "example":
       ABCDE examp
       FGHIK lbcdf
       LMNOP ghikn
       QRSTU oqrst
       VWXYZ uvwyz
       
       examp ABCDE
       lbcdf FGHIK
       ghikn LMNOP
       oqrst QRSTU
       uvwyz VWXYZ
    3. Every 2 letters from the message are indexed in the top left and bottom
       right alphabets, and their rows and columns are lined up. For example,
       with the 2 message letters "AB", the letter from the top right
       alphabet, x, and the letter from the bottom left alphabet, e, are put
       into the cipher.
    
    Returns the cipher, the top right alphabet sequence, and the bottom left
    alphabet sequence.
    '''
    
    ## Variables
    # General
    array, cipher = [], []
    numbers = bool(numbers)
    teens = [str(x) for x in range(10, 20)]
    alphabet = (list(up.replace('J', '')), list(up) + teens)[numbers]
    # Message
    message = (message.upper().replace('J', 'I'), message.upper())[numbers]
    message = [x for x in message if x in (up, up + digits)[numbers]]
    # Array
    trAlphabet = playfair_square(trPlayfairKey, numbers, numbers)
    blAlphabet = playfair_square(blPlayfairKey, numbers, numbers)
    m = (5, 6)[numbers]
    for x in range(0, m ** 2, m):
        array.append(list(alphabet[x:x + m] + trAlphabet[x:x + m]))
    for x in range(0, m ** 2, m):
        array.append(list(blAlphabet[x:x + m] + alphabet[x:x + m]))
    array = numpy.asarray(array)
    
    ## Encipher
    # Translate letter pairs
    while message[:2]:
        pair = message[:2]
        if len(pair) == 1: pair += pair
        i = numpy.where(array==pair[0].upper())
        ind1 = (i[0][0], i[1][0])
        i = numpy.where(array==pair[1].upper())
        ind2 = (i[0][1], i[1][1])
        cipher.append(array[ind1[0], ind2[1]])
        cipher.append(array[ind2[0], ind1[1]])
        del message[:2]
    # Put correct numbers in cipher
    for lInd, l in enumerate(cipher):
        if l in teens: cipher[lInd] = str(int(l) - 10)
    cipher = ''.join(cipher)
    trAlphabet = ''.join(trAlphabet)
    blAlphabet = ''.join(blAlphabet)
    
    ## Return cipher, top right alphabet, & bottom left alphabet
    return cipher, trAlphabet, blAlphabet
