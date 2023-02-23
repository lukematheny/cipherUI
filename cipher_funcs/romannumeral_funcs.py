# Import
from string import digits

# Decimal to Roman numeral
def dec_to_roman(num):

    '''Turns any positive integer into a Roman numeral.'''

    ## Variables
    # General
    num = int(num)
    romanList = [(1000000, '/M'), (900000, '/C/M'),
                 (500000, '/D'), (400000, '/C/D'),
                 (100000, '/C'), (90000, '/X/C'),
                 (50000, '/L'), (40000, '/X/L'),
                 (10000, '/X'), (9000, 'M/X'),
                 (5000, '/V'), (4000, 'M/V'),
                 (1000, 'M'), (900, 'CM'),
                 (500, 'D'), (400, 'CD'),
                 (100, 'C'), (90, 'XC'),
                 (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'),
                 (5, 'V'), (4, 'IV'),
                 (1, 'I')]

    ## Roman numeral
    romanNumeral = ''
    if num > 1000000:
        mills = num // 1000000
        romanNumeral += mills * '/M'
        num -= mills * 1000000
    while num > 0:
        for decNum, romNum in romanList:
            if num >= decNum:
                romanNumeral += romNum
                num -= decNum
                break

    ## Return Roman numeral
    return romanNumeral

# Encipher
def encipher_romannumeral(message, uppercase=True):

    '''
    encipher_romannumeral(message, uppercase=True)

    Extracts numbers from any message and replaces them with Roman numeral
    versions of the numbers.

    Arguments:
    message -- Message being enciphered
    uppercase -- True for uppercase and False for lowercase Roman numerals

    Steps:
    1. Documents the indices where numbers start and end in the message. If
       any number is above 1 billion, an exception is raised.
    2. All numbers are put into the dec_to_roman function and inserted into
       the message, joining to form the cipher.

    Returns the cipher.
    '''

    ## Variables
    # General
    message = list(str(message))
    indices = []
    uppercase = bool(uppercase)
    # Pull numbers from message
    prevLetter = ' '
    for letterInd, letter in enumerate(message + [' ']):
        if prevLetter not in digits and letter in digits:
            indBegin = letterInd
        elif prevLetter in digits and letter not in digits:
            indEnd = letterInd
            indices.append([indBegin, indEnd])
        prevLetter = letter
    for begin, end in indices:
        if int(''.join(message[begin:end])) > 1000000000:
            return print('\nNumber too large, try again.\n')

    ## Encipher
    # Make all Roman numerals
    for begin, end in reversed(indices):
        numeral = dec_to_roman(int(''.join(message[begin:end])))
        message[begin:end] = (numeral.lower(), numeral.upper())[uppercase]
    cipher = ''.join(message)

    ## Return cipher
    return cipher
