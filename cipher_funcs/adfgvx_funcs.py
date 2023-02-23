# Import
try:
    from playfair_funcs import playfair_square
    from columnartransposition_funcs import encipher_columnartransposition
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
    from .columnartransposition_funcs import encipher_columnartransposition
try:
    import numpy as notBeingUsed
except ImportError:
    print('Install numpy for the ADFGX and ADFGVX ciphers.')
from string import ascii_lowercase as low, digits

# Encipher
def encipher_adfgvx(message, transposKey, playfairKey=None):

    '''
    encipher_adfgvx(message, transposKey, playfairKey=None)

    The message is encrypted with a 6x6 Polybius square with ADFGVX instead
    of 123456, which is encrypted using columnar transposition.

    Arguments:
    message -- Message being enciphered
    transposKey -- Columnar transposition key for rearranging letters
    playfairKey -- Playfair key for the Polybius square

    Steps:
    1. A 6x6 Playfair alphabet is made, resulting in a Polybius square like:
          [A D F G V X]
       [A] a b c d e f
       [D] g h i j k l
       [F] m n o p q r
       [G] s t u v w x
       [V] y z 0 1 2 3
       [X] 4 5 6 7 8 9
    2. The letters to the left and above the message letter in the square are
       put into the cipher.
       For example, in the square above, "bar" would be AD AA FX.
    3. The new letter pairs are put into the columnar transposition cipher
       with the transposition key with no nulls.

    Returns cipher and Playfair alphabet.
    '''

    ## Variables
    # General
    letterPairs = ''
    half1 = list(''.join(x * 6 for x in 'ADFGVX'))
    # Revise message
    message = [x for x in message.lower() if x in low + digits]
    # Alphabet sequence
    alphabet = ''.join(playfair_square(playfairKey, True, True))
    ADFGVXalphabet = list(zip(alphabet, 6 * 'ADFGVX'))

    ## Encipher
    # Convert to letter pairs
    for letter in message:
        for let, half2 in ADFGVXalphabet:
            if let == letter:
                letterPairs += half1[alphabet.index(let)] + half2
                break
    # Columnar transposition
    cipher = encipher_columnartransposition(letterPairs, transposKey, False)

    ## Return cipher & alphabet
    return cipher, alphabet
