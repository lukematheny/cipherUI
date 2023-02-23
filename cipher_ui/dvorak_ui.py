# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.dvorak_funcs import encipher_dvorak, decipher_dvorak

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED('Encipher QWERTY to DVORAK (0) '
                + 'or decipher DVORAK to QWERTY (1)? ')

    # Input message/cipher
    m_c = inpText(ed=e_d)

    # Input layers
    layers = inpNum('Layers of encryption' + ('', ' (repeats at 210)')[e_d]
                    + ': ')

    # Print cipher/message
    if e_d: print('\n' + encipher_dvorak(m_c, layers) + '\n')
    else: print('\n' + decipher_dvorak(m_c, layers) + '\n')
