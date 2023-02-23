# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.caesar_funcs import encipher_caesar, decipher_caesar

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, 'let', e_d, w=False)

    # Input shift
    if not e_d: shift = inpChoice('Is the shift unknown (0) or known (1)? ',
                                  [None, True])
    if e_d or shift: shift = inpNum('Shift letters by how much? ')

    # Print cipher
    if e_d:
        print('\n' + encipher_caesar(m_c, shift) + '\n')

    # Print message(s)
    else:
        a, b = decipher_caesar(m_c, shift)
        if isinstance(a, str):
            print('\n' + a + '\n')
        elif b == None:
            print('\nPossible messages:\n' + '\n'.join(reversed(a)) + '\n')
        else:
            print('\nPossible messages:\n' + '\n'.join(reversed(a))
                  + '\n\nMost probable:\n' + '\n'.join(
                  [x[0] + ' (shift ' + str(x[1]) + ')' for x in b]
                  ) + '\n')
