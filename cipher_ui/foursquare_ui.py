# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.foursquare_funcs import encipher_foursquare

# UI
def ui():

    # Input Playfair keys
    (trKey, blKey), numbers = inpPlayfair(True, 5, True, None,
                                          [True, 'For the top right Playfair '
                                           + 'square:', 'For the bottom left '
                                           + 'Playfair square:'])

    # Input message
    message = inpText(None, ('let', 'letNum')[numbers], True)

    # Print cipher
    a, b, c = encipher_foursquare(message, trKey,
                                  blKey, numbers)
    print('\nCipher: ' + a + '\nTop right Playfair square alphabet: ' + b
          + '\nBottom left Playfair square alphabet: ' + c + '\n')
