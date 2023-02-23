# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.vigenere_funcs import encipher_vigenere

# UI
def ui():

    # Input message and keep non-letters
    message, kinl = inpText(None, 'let', knl=[True, 'let', True],
                            knlText='Should the key apply to non-letters? '
                                    + '(False recommended) ')
    
    # Input key
    key = inpText('Key: ', 'let')

    # Input form
    form = inpChoice('Form of encryption (Vigenere, Beaufort, or German): ',
                     {'v': 'v', 'vigenere': 'v', 'b': 'b', 'beaufort': 'b',
                      'g': 'g', 'german': 'g'}, False)

    # Print cipher
    print('\n' + encipher_vigenere(message, key, form, kinl) + '\n')
