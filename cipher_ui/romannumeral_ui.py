# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.romannumeral_funcs import encipher_romannumeral

# UI
def ui():
    
    # Input message
    message = inpText(None, 'digits')
    
    # Input uppercase
    uppercase = inpChoice('Uppercase (0) or lowercase (1)? ', [True, False])
    
    # Print cipher
    a = encipher_romannumeral(message, uppercase)
    if a: print('\n' + a + '\n')
    else: ui()