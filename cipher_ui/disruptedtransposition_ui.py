# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.disruptedtransposition_funcs import \
     encipher_disruptedtransposition

# UI
def ui():

    # Input message
    message = inpText()

    # Input key
    key = inpText('Key: ', 'letNum')

    # Input rows
    rows = inpChoice('Automatic number of rows (0) or specified number '
                     + 'of rows (1)? ', [None, False])
    if rows == False:
        rows = inpNum('Row number: ', max=len(message) * 10)
        if rows * len([x for x in key if x in low + digits]) < len(message):
            print('Row number too small for cipher, automated number '
                  + 'used instead.'); rows = None

    # Print cipher, enumerated cipher, and indices
    a, b, c = encipher_disruptedtransposition(message, key, rows)
    print('\nCipher: ' + a)
    if c:
        print('Enumerated cipher: ' + b)
        width = len(str(c[-1][0]))
        if width < 4:
            print('\n{:>{w}}│{}'.format('I', '#', w=width))
        else:
            print('{:{w}}│{}'.format('Index', '#', w=width))
        for index, number in c:
            print('{:{w}}│{}'.format(index, number, w=width))
    else:
        print('\nIndex│#\n None│None')
    print()
