# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
from string import ascii_lowercase as low, digits

# Encipher
def encipher_polybiussquare(message, playfairKey=None, numbers=False):
    
    '''
    encipher_polybiussquare(message, playfairKey='', numbers=False)
    
    The Playfair key is translated to an alphabet, then each letter from the
    message is turned into coordinates to form the cipher.
    
    Arguments:
    message -- Message being enciphered
    playfairKey -- Key for the playfair_square function for the sequence of 
                   letters in the grid
    numbers -- False for 5x5 square without j, True for 6x6 square with digits
    
    Steps:
    1. A Playfair square is generated from the Playfair key with the    
       playfair_square function.
    2. The sequence is lined up like:
          [1 2 3 4 5]
       [1] a b c d e
       [2] f g h i k
       [3] l m n o p
       [4] q r s t u
       [5] v w x y z
    3. The numbers to the left and above the message letter in the square are 
       put into the cipher.
       For example, in the square above, "bar" would be 12 11 42.
    
    Returns cipher and sequence.
    '''
    
    ## Variables
    # General
    cipher = ''
    numbers = bool(numbers)
    alphabet = (low[:9] + low[10:], low + digits)[numbers]
    m, n = ((5, '12345'), (6, '123456'))[numbers]
    # Message
    message = (message.lower().replace('j', 'i'), message.lower())[numbers]
    message = [x for x in message if x in alphabet]
    # Sequences
    sequence = ''.join(playfair_square(playfairKey, numbers, numbers))
    enumSequence = list(zip(m * n, sequence))
    
    ## Encipher
    for letter in message:
        for number, letter2 in enumSequence:
            if letter == letter2:
                ind = sequence.index(letter2)
                for x in range(1, m + 1):
                    if ind in range(m * (x - 1), m * x):
                        cipher += str(x) + number
                        break
                break
    
    ## Return cipher & sequence
    return cipher, sequence

# Decipher
def decipher_polybiussquare(cipher, playfairKey='', numbers=False):
    
    '''
    decipher_polybiussquare(cipher, playfairKey='', numbers=False)
    
    The Playfair key is translated to an alphabet, then each pair of 
    coordinates from the cipher is put into letters from the square as the cipher.
    
    Arguments:
    cipher -- String of coordinates to be deciphered
    playfairKey -- Key for the playfair_square function for the sequence of 
                   letters in the grid
    numbers -- True for 6x6 square with digits, False for 5x5 square without j
    
    Steps:
    1. A Playfair square is generated from the Playfair key with the    
       playfair_square function.
    2. The sequence is lined up like:
          [1 2 3 4 5]
       [1] a b c d e
       [2] f g h i k
       [3] l m n o p
       [4] q r s t u
       [5] v w x y z
    3. Where the row of the first letter and the column of the second letter in
       a pair of coordinates intersect, the letter in that position is put into
       the message.
       For example, in the cipher above, "121142" would be bar.
    
    Returns cipher and Playfair square.
    '''
    
    ## Variables
    # General
    message = ''
    numbers = bool(numbers)
    m, n = ((5, '12345'), (6, '123456'))[numbers]
    # Message
    cipher = [x for x in str(cipher) if x in n]
    # Sequences
    sequence = ''.join(playfair_square(playfairKey, numbers, numbers))
    enumSequence = list(zip(m * n, sequence))
    
    ## Decipher
    while len(cipher) >= 2:
        row, col = int(cipher[0]), int(cipher[1])
        message += sequence[(m * (row - 1) + col) - 1]
        del cipher[:2]
    
    ## Return message & sequence
    return message, sequence
