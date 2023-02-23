# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.keyword_funcs import encipher_keyword, decipher_keyword

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input keyword
    key, numbers = inpPlayfair(True, 5, True, ('Do', 'Should')[e_d] + ' the '
                               + 'alphabets have numbers (1) or not (0)? ',
                               textKey='Keyword: ', textMix='Mixed keyword '
                               + 'alphabet (0) or keyword (1)? ')

    # Input message/cipher
    m_c = inpText(None, ('let', 'letNum')[numbers], e_d)

    # Print cipher/message
    if e_d:
        a, b = encipher_keyword(m_c, key, numbers)
        print('\nCipher: ' + a + '\nKey alphabet: ' + b + '\n')
    else: print('\n' + decipher_keyword(m_c, key, numbers) + '\n')
