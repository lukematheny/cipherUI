# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.railfence_funcs import encipher_railfence, \
     decipher_railfence

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher and keepNonLetNum
    m_c = inpText(None, 'letNum', e_d, m=False, knl=[(False, True)[e_d],
                                                     'letNum', True])
    if e_d: m_c, keepNonLetNum = m_c

    # Input rails
    while True:
        rails = inpNum('Number of rails: ')
        if rails != 0: break
        print('\nRails cannot be 0, try again.\n')

    # Input starting point
    rails = eval(inpChoice(('Does', 'Should')[e_d]  + ' the message start from'
                           + ' the top rail (0) or bottom rail (1)? ',
                           ['abs(rails)', '-abs(rails)']))

    # Print cipher/message
    if e_d: print('\n' + encipher_railfence(m_c, rails, keepNonLetNum) + '\n')
    else: print('\n' + decipher_railfence(m_c, rails) + '\n')
