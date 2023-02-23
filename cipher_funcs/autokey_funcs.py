# Import
try:
    from vigenere_funcs import encipher_vigenere
except ModuleNotFoundError:
    from .vigenere_funcs import encipher_vigenere
from string import ascii_lowercase as low
import random

# Encipher
def encipher_autokey(message, key, keystream=False):

    '''
    encipher_autokey(message, key, keystream=False)

    The key length becomes equal to the message length by adding the message
    or a random string of characters, based on the keystream argument, then
    put through the Vigenere cipher.

    Arguments:
    message -- Message being enciphered
    key -- Primer to the key that is developed to equal the message's length
    keystream -- True to complement key with random letters, False to
                 complement key with the message

    Steps:
    1. If keystream is False, the message is added to the key. If True, random
       letters are added until the key and message lengths match.
    2. The message and new key are put through the Vigenere cipher using the
       function encipher_vigenere with kInNonL set to False because only
       letters are used in the key to encipher, and if the key is applied to
       the whole message, the key may not be long enough because of its
       deleted letters.

    Returns cipher and if keystream is True, the random letters are returned.
    '''

    ## Variables
    # General
    keystreamList = ''
    keystream = bool(keystream)
    # Alter key
    key = [x for x in key.lower() if x in low]
    if keystream:
        while len(key) < len(message):
            rand = random.choice(low)
            keystreamList += rand
            key += rand
    else:
        key += message
    key = ''.join(key)

    ## Encipher
    cipher = encipher_vigenere(message, key, 'v', False)

    ## Return cipher
    return ((cipher, None), (cipher, keystreamList))[keystream]
