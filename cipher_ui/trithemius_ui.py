# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.trithemius_funcs import encipher_trithemius, \
     decipher_trithemius

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message and keep non-letters
    m_c, kinl = inpText(None, 'let', e_d, False, knl=[True, 'let', True],
                        knlText=('Does', 'Should')[e_d] + ' the key apply to '
                        + 'non-letters? ' + ('', '(False recommended) ')[e_d])

    # Input start
    if not e_d:
        start = inpChoice('Is the starting integer unknown (0) '
                          + 'or known (1)? ', [None, True])
    if e_d or start:
        start = inpNum('Starting integer: ', minNum=0, maxNum=25)

    # Input ascend/descend
    if not e_d:
        ascend = inpChoice('Is ascension/descension unknown (0) '
                           + 'or known (1)? ', [None, True])
    if e_d or ascend:
        ascend = inpChoice(('Do', 'Should')[e_d] + ' the numbers ascend (0) or'
                           + ' descend (1)? ', [True, False])

    # Print cipher
    if e_d: print('\n' + encipher_trithemius(m_c, start, ascend, kinl) + '\n')

    # Print message(s)
    else:
        a, b = decipher_trithemius(m_c, start, ascend, kinl)

        ## Actual messages
        if isinstance(a, str):
            print('\n' + a + '\n')

        ## Possible messages
        else:
            print('\nPossible messages:')
            if start == None:
                # Print nums and directions
                if ascend == None:
                    nums = [z for y in [[f'{x:02}', f'{x:02}']
                            for x in range(26)] for z in y]
                    for x, y, z in zip(nums, '↑↓' * 26, a):
                        print(x + y + ': ' + z)
                # Print only nums
                else:
                    for x, y in zip([f'{x:02}' for x in range(26)], a):
                        print(x + ': ' + y)
            # Print only directions
            else:
                for x, y in zip('↑↓', a):
                    print(x + ': ' + y)

            ## Probable messages
            if b != None:
                print('\nMost probable:')
                for x, y, z in b:
                    if start == None:
                        # Print nums and directions
                        if ascend == None:
                            print(y + z + ': ' + x)
                        # Print only nums
                        else:
                            print(y + ': ' + x)
                    # Print only directions
                    else:
                        print(z + ': ' + x)
            print()
