# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.autokey_funcs import encipher_autokey

# UI
def ui():

    # Input message
    message = inpText(None, 'let', w=False)

    # Input key
    key = inpText('Key: ', 'let', w=False)

    # Input keystream
    if len([x for x in message if x in let]) \
    > len([x for x in key if x in let]):
        keystream = inpYN('Keystream (random letters) for key remainder? ')
    else:
        keystream = False

    # Print cipher
    a, b = encipher_autokey(message, key, keystream)
    if b: print('\nCipher: ' + a + '\nKeystream: ' + b + '\n')
    else: print('\n' + a + '\n')
