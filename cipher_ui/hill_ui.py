# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.hill_funcs import encipher_hill

# UI
def ui():

    # Note
    print('Note: The message and key will be repeated to extend their lengths '
          + 'if their lengths are not perfect squares.')

    # Message
    message, binary = inpList('message')

    # Key
    key, binary = inpList('key')

    # Print cipher
    a, b = encipher_hill(message, key)
    print('\nCipher number list: ' + str(a) + '\nCipher: ' + b + '\n')
