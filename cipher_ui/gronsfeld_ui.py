# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.gronsfeld_funcs import encipher_gronsfeld

# UI
def ui():

    # Input message and keep non-letters
    message, kinl = inpText(None, 'let', m=False, knl=[True, 'let', True],
                           knlText='Should the key apply to non-letters? '
                                   + '(False recommended) ')

    # Input key
    key = inpText('Key: ', 'digits')

    # Print cipher
    print('\n' + encipher_gronsfeld(message, key, kinl) + '\n')
