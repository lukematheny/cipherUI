# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.polybiussquare_funcs import encipher_polybiussquare, \
     decipher_polybiussquare

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input Playfair key
    playfairKey, numbers = inpPlayfair(True, 5, True)

    # Input message/cipher
    m_c = inpText(None, (('12345', '123456')[numbers],
                         ('let', 'letNum')[numbers])[e_d], e_d)

    # Print cipher/message and sequence
    if e_d:
        a, b = encipher_polybiussquare(m_c, playfairKey, numbers)
        print('\nCipher: ' + a + '\nSequence: ' + b + '\nGrid:\n   '
              + '[1 2 3 4 5' + ('', ' 6')[numbers] + ']')
    else:
        a, b = decipher_polybiussquare(m_c, playfairKey, numbers)
        print('\nMessage: ' + a + '\nSequence: ' + b + '\nGrid:\n   ')
    f, g = (('12345', 5), ('123456', 6))[numbers]
    for x, y in zip(f, [b[z:z+g] for z in range(0, len(b), g)]):
        print('[' + x + '] ' + ' '.join(y))
    print()
