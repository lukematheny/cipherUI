# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.bacon_funcs import encipher_bacon, decipher_bacon

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, 'let', e_d, w=(False, True)[e_d])

    # Print cipher/message
    if e_d: print('\n' + encipher_bacon(m_c) + '\n')
    else:
        a = decipher_bacon(m_c)
        if a: print('\n' + a + '\n')
