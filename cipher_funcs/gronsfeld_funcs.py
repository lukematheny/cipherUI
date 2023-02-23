# Import
try:
    from vigenere_funcs import encipher_vigenere
except ModuleNotFoundError:
    from .vigenere_funcs import encipher_vigenere
from string import ascii_lowercase as low, digits

# Encipher
def encipher_gronsfeld(message, key, kInNonL=False):

    '''
    encipher_gronsfeld(message, key, kInNonL=False)

    The key numbers are converted to letters, and are put with the message
    through the Vigenere cipher.

    Arguments:
    message -- Message being enciphered
    key -- Sequence of numbers used as Vigenere key, non-numbers are taken out
    kInNonL -- False for the key to only apply to letters, otherwise True

    Steps:
    1. The non-numbers are taken out of the key. The remaining numbers are
       converted to letters based on a = 0 and j = 9.
    2. The message, key, and kInNonL arguments are put through the Vigenere
       cipher, with form as 'vigenere', to produce the cipher.

    Returns the cipher.
    '''

    ## Variables
    key = [low[int(x)] for x in key if x in digits]

    ## Encipher
    cipher = encipher_vigenere(message, key, 'v', kInNonL)

    ## Return cipher
    return cipher
