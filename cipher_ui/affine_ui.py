# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.affine_funcs import encipher_affine, decipher_affine, \
     coprime26

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, 'let', e_d, w=(False, True)[e_d])

    # Input A and B
    while True:
        a = inpNum('A: ')
        if coprime26(a): break
        print("\nA must be a coprime of 26, try again.\n")
    b = inpNum('B: ')

    # Print cipher/message
    if e_d: print('\n' + encipher_affine(m_c, a, b) + '\n')
    else: print('\n' + decipher_affine(m_c, a, b) + '\n')
