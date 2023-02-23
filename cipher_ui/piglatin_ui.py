# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.piglatin_funcs import encipher_piglatin

# UI
def ui():
    
    # Input message
    message = inpText(None, 'let', w=False)
    
    # Input vStartAsC
    vStartAsC = inpChoice('Should the words beginning with vowels be kept but '
                          + "with 'way' at the end (0) or should the first "
                          + 'group of vowels be ignored and interpreted as '
                          + 'consonants (1)? (1 recommended — See '
                          + 'documentation) ')
    
    # Print cipher
    print('\n' + encipher_piglatin(message, vStartAsC) + '\n')