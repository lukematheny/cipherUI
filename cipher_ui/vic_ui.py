# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.vic_funcs import encipher_vic, decipher_vic

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, ('let', '/.'), e_d, m=False)

    # Input addKey/subtractKey
    a_sKey = inpText(('Subtract', 'Add')[e_d] + ' key: ', 'digits')

    # Input numKey
    numKey, a = inpPlayfair(True, textMix='Mixed alphabet (0) or Playfair key'
                            + ' (1) for horizontal axis coordinates (string of'
                            + ' numbers 0-9)? ')

    # Input numExclude
    numExclude = inpNum('Two numbers for vertical axis coordinates: ', minLen=2)
    if len(str(numExclude)) > 2: print('Only first two numbers will be used.')

    # Input row1key and remainKey
    (row1key, remainKey), a = inpPlayfair(True, twice=[True, 'For the top '
                                          + "row (characters in 'restonia'):",
                                          "For the grid's remainder (alphabet"
                                          + ' including / and .):'])

    # Print cipher/message and grid
    func = (decipher_vic, encipher_vic)[e_d]
    a, b = func(m_c, a_sKey, numKey, numExclude, row1key, remainKey)
    print('\n' + ('Message', 'Cipher')[e_d] + ': ' + a + '\nGrid:\n'
          + str(b)[1:-1].replace("'", '').replace('\n ', '\n') + '\n')
