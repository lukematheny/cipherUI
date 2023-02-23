# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.adfgx_funcs import encipher_adfgx

# UI
def ui():

    # Input message
    message = inpText(None, 'let', True)

    # Input transposition key
    transposKey = inpText('Transposition key: ', 'letNum', w=False)

    # Input alphabet
    playfairKey, a = inpPlayfair(True)

    # Print cipher and alphabet
    a, b = encipher_adfgx(message, transposKey, playfairKey)
    print('\nCipher: ' + a + '\nSequence: ' + b + '\nGrid:\n   [A D F G X]')
    for x, y in zip('ADFGX', [b[z:z+5] for z in range(0, len(b), 5)]):
        print('[' + x + '] ' + ' '.join(y))
    print()
