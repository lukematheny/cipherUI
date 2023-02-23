# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.chaocipher_funcs import encipher_chaocipher

# UI
def ui():

    # Input Playfair key
    (plain, ciph), numbers = inpPlayfair(True, 5, True, '26 letter Playfair '
                                         + 'keys (0) or 36 letter/number'
                                         + ' Playfair keys (1)? ', [True,
                                         '\nFor plaintext alphabet:',
                                         '\nFor ciphertext alphabet:'])

    # Input message
    message = inpText(None, ('let', 'letNum')[numbers])

    # Print cipher & alphabets
    a, b, c = encipher_chaocipher(message, plain, ciph, numbers)
    print('\nCipher: ' + a + '\nPlaintext alphabet: ' + b
          + '\nCiphertext alphabet: ' + c + '\n')
