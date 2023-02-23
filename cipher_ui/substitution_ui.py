# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.substitution_funcs import encipher_substitution, \
     decipher_substitution

# UI
def ui():
    
    # Input encipher/decipher
    e_d = inpED()
    
    # Input message/cipher
    m_c = inpText(ed=e_d)
    
    # Input Playfair key
    playfairKey, numbers = inpPlayfair(True, 5, True)
    
    # Print cipher/message
    if e_d:
        a, b = encipher_substitution(m_c, playfairKey, numbers)
        print('\nCipher: ' + a + '\nKey alphabet: ' + b + '\n')
    else:
        a, b = decipher_substitution(m_c, playfairKey, numbers)
        print('\nMessage: ' + a + '\nKey alphabet: ' + b + '\n')