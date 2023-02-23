# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.fractionatedmorse_funcs import encipher_fractionatedmorse, \
     decipher_fractionatedmorse

# UI
def ui():
    
    # Input encipher/decipher
    e_d = inpED()
    
    # Input message/cipher
    m_c = inpText(ed=e_d)
    
    # Input Playfair key
    playfairKey, a = inpPlayfair(True)
    
    # Encipher/decipher
    if e_d:
        a, b, c = encipher_fractionatedmorse(m_c, playfairKey)
        print('\nCipher: ' + a + '\nTable: ')
    else:
        a, b, c = decipher_fractionatedmorse(m_c, playfairKey)
        print('\nMessage: ' + a + '\nTable: ')
    c = [(x[0], x[1][0], x[1][1], x[1][2]) for x in c]
    print(''.join(x[0] for x in c))
    print(''.join(x[1] for x in c))
    print(''.join(x[2] for x in c))
    print(''.join(x[3] for x in c))
    print()