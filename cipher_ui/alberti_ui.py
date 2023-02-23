# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.alberti_funcs import encipher_alberti_method1, \
     encipher_alberti_method2

# UI
def ui():

    # Input method 1 or 2, True for method1
    method = inpMethod()

    # Input message
    message = inpText(None, ('letNum', ('let', '1234'))[method], True)

    # Input key letter
    if not method:
        key = inpChr('Key letter: ', 'ABCDEFGILMNOPQRSTVXZ1234', True,
                     '\nMust be random or in key list, try again.'
                     + '\nKey list = ABCDEFGILMNOPQRSTVXZ1234\n', True)

    # Input pointer letter
    pointer = inpChr('Pointer letter: ', 'klnprtvz&xysomqihfdbaceg', True,
                     '\nMust be random or in value list, try again.'
                     + '\nValue list = klnprtvz&xysomqihfdbaceg\n', True)

    # Input direction
    if not method:
        direction = inpChoice('Direction of spin: ', {'c': 'c', 'clockwise':
                              'c', 'cc': 'cc', 'counterclockwise': 'cc',
                              'rand': 'random', 'random': 'random'},
                              False, '\nDirection needs to be clockwise or '
                              + 'counterclockwise, try again.\n')

    # Input ampersand replacement
    ampRep = inpChr('Ampersand replacement: ', 'juw', True,
                    '\nMust be j, u, w, or random.\n', True)

    # Print cipher for method 1
    if method:
        a, b, c = encipher_alberti_method1(message, pointer, ampRep)
        if b or c:
            print('\nCipher: ' + a)
            if b: print('Pointer letter: ' + b)
            if c: print('Ampersand replacement: ' + c)
        else: print('\n' + a)
        print()

    # Print cipher for method 2
    else:
        a, b, c, d, e, f = encipher_alberti_method2(message, key, pointer,
                                                 direction, ampRep)
        if a == None: ui()
        else:
            print('\nCipher: ' + a)
            if b: print('Pointer letter: ' + b)
            if c: print('Key letter: ' + c)
            if d: print('Direction: ' + d)
            if e: print('Ampersand replacement: ' + e)
            print()
            width = max([len(str(x)) for x, y in f])
            print('{:>{w}}│{}'.format(('Index', 'I')[width < 4],
                                      '#', w=width))
            for index, number in f:
                print('{:{w}}│{}'.format(index, number, w=width))
            print()
