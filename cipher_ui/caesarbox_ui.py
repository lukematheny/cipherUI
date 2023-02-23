# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.caesarbox_funcs import encipher_caesarbox, \
     decipher_caesarbox

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c = inpText(None, 'letNum', e_d, False, (False, True)[e_d],
                  knl=[(False, True)[e_d], 'letNum', True])
    if e_d: m_c, keepNonLetNum = m_c

    # Input rows and nulls
    while True:
        rows = inpNum('Rows: ')
        if rows == 0: print('\nRows cannot be 0, try again.\n'); continue
        if rows > len(m_c) * 2:
            print('\nNumber too large, try again.\n'); continue
        break
    rows = eval(inpChoice(('Does', 'Should')[e_d] + ' the message start from '
                          'the top row (0) or bottom row (1)? ', ['abs(rows)',
                          '-abs(rows)']))
    if e_d and (len([x for x in m_c if x in letNum]),
                len(m_c))[keepNonLetNum] % rows != 0:
        nulls = inpYN('Insert nulls into blank spaces? ')
    else: nulls = False

    # Print cipher/message and array
    if e_d:
        a, b = encipher_caesarbox(m_c, rows, nulls, keepNonLetNum)
        print('\nCipher: ' + a + '\nGrid:\n' + str(b).replace("'", ''))
    else:
        a, b = decipher_caesarbox(m_c, rows)
        print('\nMessage: ' + a + '\nGrid:\n' + str(b).replace("'", ''))
    print()
