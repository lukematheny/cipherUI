# Import
try:
    from playfair_funcs import playfair_square
    from columnartransposition_funcs import encipher_columnartransposition
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
    from .columnartransposition_funcs import encipher_columnartransposition
from string import ascii_lowercase as low

# Encipher
def encipher_adfgx(message, transposKey, playfairKey=None):

    '''
    encipher_adfgx(message, transposKey, playfairKey=None)

    The message is encrypted with a 5x5 Polybius square with ADFGX instead of
    12345, which is encrypted using columnar transposition.

    Arguments:
    message -- Message being enciphered
    transposKey -- Columnar transposition key for rearranging letters
    playfairKey -- Playfair key for the Polybius square

    Steps:
    1. A 5x5 Playfair alphabet is made, resulting in a Polybius square like:
          [A D F G X]
       [A] a b c d e
       [D] f g h i k
       [F] l m n o p
       [G] q r s t u
       [X] v w x y z
       Note that j is left out to keep a 5x5 square. Any j in the message
       will be turned to an i.
    2. The letters to the left and above the message letter in the square are
       put into the cipher.
       For example, in the square above, "bar" would be AD AA GD.
    3. The new letter pairs are put into the columnar transposition cipher
       with the transposition key with no nulls.

    Returns cipher and Playfair alphabet.
    '''

    ## Variables
    # General
    letterPairs = ''
    half1 = list(''.join(x * 5 for x in 'ADFGX'))
    # Revise message
    message = [x for x in message.lower().replace('j', 'i') if x in low]
    # Alphabet sequence
    alphabet = ''.join(playfair_square(playfairKey))
    ADFGXalphabet = list(zip(alphabet, 5 * 'ADFGX'))

    ## Encipher
    # Convert to letter pairs
    for letter in message:
        for let, half2 in ADFGXalphabet:
            if let == letter:
                letterPairs += half1[alphabet.index(let)] + half2
                break
    # Columnar transposition
    cipher = encipher_columnartransposition(letterPairs, transposKey, False)

    ## Return cipher & alphabet
    return cipher, alphabet
