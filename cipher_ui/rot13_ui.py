# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.rot13_funcs import encipher_rot13, decipher_rot13

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, 'let', e_d, w=False)

    # Print cipher/message
    print('\n' + encipher_rot13(m_c) + '\n')
