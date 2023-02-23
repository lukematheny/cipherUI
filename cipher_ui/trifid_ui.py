# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.trifid_funcs import encipher_trifid, decipher_trifid

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, ('let', '+'), e_d)

    # Input Playfair key
    playfairKey, a = inpPlayfair(True)

    # Input group size
    size = inpNum('Letter grouping size: ', minNum=1)

    # Print cipher/message
    if e_d:
        a, b, c = encipher_trifid(m_c, playfairKey, size)
        print('\nCipher: ' + a + '\nSequence: ' + b + '\nGrid:\n'
              + str(c).replace("'", '') + '\n')
    else:
        a, b, c = decipher_trifid(m_c, playfairKey, size)
        print('\nMessage: ' + a + '\nSequence: ' + b + '\nGrid:\n'
              + str(c).replace("'", '') + '\n')
