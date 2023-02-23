# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.route_funcs import encipher_route, decipher_route
from math import sqrt

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    while True:
        m_c = inpText(None, (None, 'letNum')[e_d], e_d,
                      m=False, knl=[True, 'letNum', True])
        if e_d: m_c, kNLN = m_c
        else: kNLN = True
        length = (len([x for x in m_c if x in letNum]), len(m_c))[kNLN]
        if length == 0:
            print('\nThe message cannot have a length of zero, try again.\n')
        else:
            break

    # Input rows
    rows = (False, None)[inpYN('Automatic number of rows? ')]
    if rows == False:
        rows = inpNum('Number of rows: ', maxNum=length)

    # Input write and read
    if not e_d:
        print('Note: When deciphering, write and read are how they were '
              + 'originally written and read when they were enciphered.')
    for x in range(2):
        print('For ' + ('write', 'read')[x == 1] + ' (Check syntax in '
              + 'encipher_route docstring for details):')
        if e_d: w_r = (False, None)[inpYN('Random sequence? ')]
        else: w_r = False
        if w_r == False:
            first = inpChoice('First variable - Pattern:\n0 = Zigzag\n1 = '
                              + 'Snake\n2 = Spiral\nNumber: ',
                              ['z', 's', 'sp'])
            second = inpChoice('Second variable - Starting direction:\n0 = '
                               + 'Horizontal\n1 = Vertical\nNumber: ',
                               ['h', 'v'])
            third = inpChoice('Third variable - Starting point:\n0 = Top '
                              + 'left\n1 = Top right\n2 = Bottom left\n3 = '
                              + 'Bottom right\nNumber: ',
                              ['tl', 'tr', 'bl', 'br'])
            w_r = ';'.join((first, second, third))
        if x == 0: write = w_r
        else: read = w_r

    # Input appendage
    if e_d and length % (rows, round(sqrt(length) / 1.5))[rows == None] != 0:
        appendage = inpChoice('In case the message needs to be lengthened, '
                              + 'what should be appended to it?\n0 = '
                              + 'Lowercase letters\n1 = Uppercase letters\n2 '
                              + '= All letters\n3 = Numbers\n4 = Lowercase '
                              + 'letters & numbers\n5 = Uppercase letters & '
                              + 'numbers\n6 = All letters & '
                              + 'numbers\nNumber: ', ['low', 'up', 'let',
                              'digits', 'low + digits', 'up + digits', 'let '
                              + '+ digits'])
    else: appendage = 'let'

    # Print for encipher/decipher
    if e_d:
        a, b, c, d, e = encipher_route(m_c, write, read, rows, kNLN, appendage)
        print('\nCipher: ' + a + '\nGrid:\n'
              + str(b).replace("'", '').replace('""', "'"))
        print('Write: ' + c)
        print('Read: ' + d)
        if e != '': print('Appended: ' + e)
    else:
        a, b = decipher_route(m_c, write, read, rows)
        print('\nMessage: ' + a + '\nGrid:\n'
              + str(b).replace("'", '').replace('""', "'"))
    print()
