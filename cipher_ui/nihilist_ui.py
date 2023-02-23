# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.nihilist_funcs import encipher_nihilist

# UI
def ui():

    # Input Playfair key
    playfairKey, numbers = inpPlayfair(True, 5, True)

    # Input message
    message = inpText(None, ('let', 'letNum')[numbers])

    # Input key
    key = inpText('Key: ', ('let', 'letNum')[numbers])

    # List or string
    listReturn = inpChoice('Return string of numbers (0) or list of '
                           + 'numbers (1)? ')

    # Print cipher and sequence
    a, b = encipher_nihilist(message, key, playfairKey, numbers, listReturn)
    print('\nCipher:', a); print('Sequence: ' + b + '\n')
