# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.doubletransposition_funcs import \
     encipher_doubletransposition

# UI
def ui():

    # Input message and keep non-letters
    while True:
        message, knl = inpText(None, 'let', m=False, knl=[True, 'let', True])
        if not knl and all(x not in let for x in message):
            print('\nMessage must have letters if non-letters are not kept'
                  + ' in encryption, try again.\n')
        else: break

    # Input keys
    key1 = inpText('Key 1: ', 'letNum')
    key2 = inpText('Key 2: ', 'letNum')

    # Input nulls
    nulls = inpYN('Insert nulls into blank spaces? ')

    # Print cipher
    print('\n' + encipher_doubletransposition(message, key1, key2,
                                              nulls, knl) + '\n')
