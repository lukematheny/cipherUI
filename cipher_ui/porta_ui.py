# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.porta_funcs import encipher_porta, decipher_porta

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher and key in non-letter
    m_c, kinl = inpText(None, 'let', ed=e_d, knl=[True, 'let', True],
                        knlText='Should the key apply to non-letters? '
                                + '(False recommended) ')

    # Input key
    key = inpText('Key: ', 'let')

    # Input alphabet type
    alphType = inpChoice('Alphabet 1 or 2? ', {'1': True, 'one': True,
                                               '2': False, 'two': False}, 0)

    # Print cipher
    if e_d: print('\n' + encipher_porta(m_c, key, alphType, kinl) + '\n')
    else: print('\n' + decipher_porta(m_c, key, alphType, kinl) + '\n')
