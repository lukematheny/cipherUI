# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.myszkowskitransposition_funcs import \
     encipher_myszkowskitransposition

# UI
def ui():

    # Input message and keep non-letters
    while True:
        message, knl = inpText(None, 'let', m=False, knl=[True, 'let', True])
        if not knl and all(x not in let for x in message):
            print('\nMessage must have letters if non-letters are not kept'
                  + ' in encryption, try again.\n')
        else: break

    # Input key
    key = inpText('Key: ', 'letNum')

    # Input nulls
    nulls = inpYN('Insert nulls into blank spaces? ')

    # Print cipher
    print('\n' + encipher_myszkowskitransposition(message, key,
                                                  nulls, knl) +'\n')
