# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.adfgvx_funcs import encipher_adfgvx

# UI
def ui():

    # Input message
    message = inpText(None, 'letNum', True)

    # Input transposition key
    transposKey = inpText('Transposition key: ', 'letNum', w=False)

    # Input alphabet
    playfairKey, a = inpPlayfair(True)

    # Print cipher and alphabet
    a, b = encipher_adfgvx(message, transposKey, playfairKey)
    print('\nCipher: ' + a + '\nSequence: ' + b + '\nGrid:\n   [A D F G V X]')
    for x, y in zip('ADFGVX', [b[z:z+6] for z in range(0, len(b), 6)]):
        print('[' + x + '] ' + ' '.join(y))
    print()
