# Import
try:
    import numpy
except ImportError:
    print('Install numpy for the Two Square cipher.')
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
from string import ascii_lowercase as low, digits
from random import choice

# Encipher
def encipher_twosquare(message, tKey=None, bKey=None, numbers=False):
    
    '''
    encipher_twosquare(message, tKey=None, bKey=None, numbers=False)
    
    The Playfair cipher is done with 2 Playfair squares instead of one.
    
    Arguments:
    message -- Message being enciphered
    tKey -- Playfair key to the top square
    bKey -- Playfair key to the bottom square
    numbers -- False for 5x5 Playfair keys, True for 6x6 Playfair keys
    
    Steps:
    1. Non-letters (and non-numbers if numbers is False) are taken out of the
       message, 'j's are replaced with 'i's if numbers is False.
    2. The message is put into pairs of adjacent letters. If the message has
       an odd number of letters, a random letter is added.
    3. Two Playfair squares are created, one top and one bottom, from the tKey
       and bKey arguments.
    4. The pair of letters from the message are put into the squares, the
       first letter to the top and the second letter to the bottom square.
    5. If the letters align vertically, they are shifted down, rotating back
       within their square if there is no letter below the original. The new
       letters are put into the cipher.
    6. If the letters don't align vertically, their intersections are put into
       the cipher with the top letter coming first.
    7. Steps 4-6 are repeated until the cipher is complete.
    
    Returns the cipher, the top alphabet, and the bottom alphabet.
    '''
    
    ## Variables
    # General
    cipher = []
    numbers = bool(numbers)
    n = (5, 6)[numbers]
    # Message
    message = (message.lower().replace('j', 'i'), message.lower())[numbers]
    message = [x for x in message if x in (low, low + digits)[numbers]]
    message = [message[x:x + 2] for x in range(0, len(message), 2)]
    if len(message[-1]) == 1: message[-1].append(choice(low))
    for xInd, x in enumerate(message):
        if x[1] in digits: message[xInd][1] = str(int(x[1]) + 10)
        else: message[xInd][1] = x[1].upper()
    # Key arrays
    tSeq = ''.join(playfair_square(tKey, numbers, numbers))
    bSeq = ''.join(playfair_square(bKey, numbers, numbers))
    tempSeq = []
    for x in bSeq:
        if x in digits: tempSeq.append(str(int(x) + 10))
        else: tempSeq.append(x.upper())
    sequence = list(tSeq) + tempSeq
    key = numpy.array([sequence[x:x + n] for x in range(0, len(sequence), n)])
    
    ## Encipher
    for letter1, letter2 in message:
        first, second = numpy.where(key==letter1), numpy.where(key==letter2)
        x1, y1, x2, y2 = first[0], first[1], second[0], second[1]
        # Shift down
        if y1 == y2:
            x1 += 1; x2 += 1
            if x1 == n: x1 = 0
            if x1 == n * 2: x1 = n
            if x2 == n: x2 = 0
            if x2 == n * 2: x2 = n
            cipher += list(key[x1, y1])
            cipher += list(key[x2, y2])
        # Intersections
        else:
            cipher += list(key[x1, y2])
            cipher += list(key[x2, y1])
    for xInd, x in enumerate(cipher):
        if len(x) == 2: cipher[xInd] = str(int(x) - 10)
    cipher = ''.join(cipher).lower()
    
    ## Return cipher, top sequence, & bottom sequence
    return cipher, tSeq, bSeq

# Decipher
def decipher_twosquare(cipher, tKey, bKey, numbers=False):
    
    '''
    decipher_twosquare(cipher, tKey, bKey, numbers=False)
    
    The Playfair cipher is done with 2 Playfair squares instead of one.
    
    Arguments:
    cipher -- Cipher being enciphered
    tKey -- Playfair key to the top square
    bKey -- Playfair key to the bottom square
    numbers -- False for 5x5 Playfair keys, True for 6x6 Playfair keys
    
    Steps:
    1. The steps to encipher_twosquare are done, outputting a message.
    2. The only deviation is that instead of the letters shifting down in step
       5, the letters shift up, rotating back within their square if there is
       no letter above the original.
    
    Returns the message, the top alphabet, and the bottom alphabet.
    '''
    
    ## Variables
    # General
    message = []
    numbers = bool(numbers)
    n = (5, 6)[numbers]
    # Cipher
    cipher = (cipher.lower().replace('j', 'i'), cipher.lower())[numbers]
    cipher = [x for x in cipher if x in (low, low + digits)[numbers]]
    cipher = [cipher[x:x + 2] for x in range(0, len(cipher), 2)]
    for xInd, x in enumerate(cipher):
        if x[1] in digits: cipher[xInd][1] = str(int(x[1]) + 10)
        else: cipher[xInd][1] = x[1].upper()
    # Key arrays
    tSeq = ''.join(playfair_square(tKey, numbers, numbers))
    bSeq = ''.join(playfair_square(bKey, numbers, numbers))
    tempSeq = []
    for x in bSeq:
        if x in digits: tempSeq.append(str(int(x) + 10))
        else: tempSeq.append(x.upper())
    sequence = list(tSeq) + tempSeq
    key = numpy.array([sequence[x:x + n] for x in range(0, len(sequence), n)])
    
    ## Decipher
    for letter1, letter2 in cipher:
        first, second = numpy.where(key==letter1), numpy.where(key==letter2)
        x1, y1, x2, y2 = first[0], first[1], second[0], second[1]
        # Shift up
        if y1 == y2:
            x1 -= 1; x2 -= 1
            if x1 == n - 1: x1 = 2 * n - 1
            if x1 == -1: x1 = n - 1
            if x2 == n - 1: x2 = 2 * n - 1
            if x2 == -1: x2 = n - 1
            message += list(key[x1, y1])
            message += list(key[x2, y2])
        # Intersections
        else:
            message += list(key[x1, y2])
            message += list(key[x2, y1])
    for xInd, x in enumerate(message):
        if len(x) == 2: message[xInd] = str(int(x) - 10)
    message = ''.join(message).lower()
    
    ## Return message, top sequence, & bottom sequence
    return message, tSeq, bSeq