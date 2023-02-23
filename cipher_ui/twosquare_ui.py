# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.twosquare_funcs import encipher_twosquare, \
     decipher_twosquare

# UI
def ui():
    
    # Input encipher/decipher
    e_d = inpED()
    
    # Input Playfair keys
    (tKey, bKey), numbers = inpPlayfair(True, 5, True, twice=[True,
                                        'For top Playfair square:',
                                        'For bottom Playfair square:'])
    
    # Input message/cipher
    m_c = inpText(None, ('let', 'letNum')[numbers], e_d)
    
    # Print cipher/message and alphabets
    if e_d:
        a, b, c = encipher_twosquare(m_c, tKey, bKey, numbers)
        print('\nCipher: ' + a + '\nTop Playfair alphabet: ' + b
              + '\nBottom Playfair alphabet: ' + c + '\n')
    else:
        a, b, c = decipher_twosquare(m_c, tKey, bKey, numbers)
        print('\nMessage: ' + a + '\nTop Playfair alphabet: ' + b
              + '\nBottom Playfair alphabet: ' + c + '\n')