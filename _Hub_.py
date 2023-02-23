# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
import cipher_funcs
from ciphers import *
from ciphers.__init__ import call, __all__
from string import ascii_uppercase as up
import random

# Spacing
def space(words):
    '''Inserts spaces into a string of capitalized words.'''
    words, indices, prevLetter = list(words), [], 'A'
    for index, letter in enumerate(words):
        if letter in up and prevLetter not in up + ' ': indices.append(index)
        prevLetter = letter
    for index in reversed(indices): words.insert(index, ' ')
    return ''.join(words)

# Docstring trim
def trimdoc(doc):
    '''Trims leading whitespace (4 chr) in docstrings.'''
    return '\n'.join(line[4:] for line in doc.split('\n'))

# Variables
cAll = ['all', 'all ciphers', 'every', 'every cipher']
cNo = ['0', 'n', 'no', 'zero', 'false']
cYes = ['1', 'ok', 'okay', 'one', 'y', 'yeah', 'yes', 'true']
cRand = ['any', 'r', 'rand', 'random']
notRec = '\nNot recognized, try again.\n'
cipherList = list(enumerate([space(x) for x in __all__], 1))
dupCipherList = []
dupCipherList[:] = cipherList
dupCipherList.append((None, None))

# Loop
while True:

    # Print ciphers
    half = len(dupCipherList) // 2
    width = max([len(y) for x, y in dupCipherList[:half]]) + 3
    for f, s in zip(dupCipherList[:half], dupCipherList[half:]):
        if s[1]:
            print(f'{f[0]:02}' + ' = ' + f[1]
                  + (width - len(f[1])) * ' '
                  + f'{s[0]:02}' + ' = ' + s[1])
        else:
            print(f'{f[0]:02}' + ' = ' + f[1])
    print()

    # Input cipher
    while True:
        cipher = input('Which cipher to use? ').lower()
        if cipher in cRand:
            cipher = random.choice(__all__)
            break
        elif cipher in cAll:
            print(call)
            continue
        else:
            try: cipher = int(float(cipher))
            except ValueError: cipher = cipher.lower().replace(' ', '')
            for num, ciph in cipherList:
                if cipher in (num, ciph.lower()):
                    cipher = ciph.replace(' ', '')
                    break
            if cipher in __all__:
                break
        print(notRec)

    # Print docstring(s)
    lowCiph = cipher.lower()
    print('\n~' + space(cipher) + (' Cipher', '')[cipher.endswith('ipher')]
          + '~\n\n' + 79 * '-')
    try:
        eval('print(trimdoc(cipher_funcs.' + lowCiph
             + '_funcs.encipher_' + lowCiph + '.__doc__))')
        print(79 * '-')
        try:
            eval('print(trimdoc(cipher_funcs.' + lowCiph
                 + '_funcs.decipher_' + lowCiph + '.__doc__))')
            print(79 * '-')
        except AttributeError:
            pass
    except AttributeError:
        eval('print(trimdoc(cipher_funcs.' + lowCiph
             + '_funcs.encipher_' + lowCiph + '_method1.__doc__))')
        print(79 * '-')
        eval('print(trimdoc(cipher_funcs.' + lowCiph
             + '_funcs.encipher_' + lowCiph + '_method2.__doc__))')
        print(79 * '-')
    print()

    # Evaluate cipher
    eval(cipher + '.main()')

    # Input loop
    while True:
        loop = input('New cipher? ').lower()
        if loop in cNo + cYes: break
        else: print(notRec)
    if loop in cNo: break
    print()
