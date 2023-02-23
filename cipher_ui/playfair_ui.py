# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.playfair_funcs import encipher_playfair, decipher_playfair

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input numbers
    key, numbers = inpPlayfair(True, 5, True, '5x5 key (0) or 6x6 key (1)? ',
                               textKey='Key: ', textMix='Mixed alphabet (0) or '
                               + 'key (1)? ')

    # Input message/cipher
    m_c = inpText(None, ('let', 'letNum')[numbers], e_d)

    # Print cipher/message, sequence, and key
    if e_d:
        a, b, c = encipher_playfair(m_c, key, numbers)
        print('\nCipher: ' + a + '\nSequence: ' + b + '\nGrid:\n'
              + str(c).replace("'", '') + '\n')
    else:
        a, b, c = decipher_playfair(m_c, key, numbers)
        print('\nMessage: ' + a + '\nSequence: ' + b + '\nGrid:\n'
              + str(c).replace("'", '') + '\n')
