# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.bifid_funcs import encipher_bifid, decipher_bifid

# UI
def ui():
    
    # Input encipher/decipher
    e_d = inpED()
    
    # Playfair key
    playfairKey, numbers = inpPlayfair(True, 5, True)
    
    # Message/cipher
    m_c = inpText(None, ('let', 'letnum')[numbers], e_d)
        
    # Print cipher/message
    if e_d:
        a, b = encipher_bifid(m_c, playfairKey, numbers)
        print('\nCipher: ' + a + '\nAlphabet: ' + b + '\n')
    else:
        a, b = decipher_bifid(m_c, playfairKey, numbers)
        print('\nMessage: ' + a + '\nAlphabet: ' + b + '\n')