# Import
try:
    from romannumeral_funcs import encipher_romannumeral
except ModuleNotFoundError:
    from .romannumeral_funcs import encipher_romannumeral
from string import ascii_lowercase as low, ascii_uppercase as up
import random

# Encipher method one
def encipher_alberti_method1(message, pointerLetter='random', ampRep='random'):

    '''
    encipher_alberti_method1(message, pointerLetter='random', ampRep='random')

    Two circles of letters are aligned and translated from the message to the
    cipher, and rotated according to the first letter and any capital letters,
    according to the pointer letter.

    Arguments:
    message -- Message being enciphered
    pointerLetter -- Value list circle letter aligned with each altering letter
    ampRep -- Letter to replace each ampersand in the final cipher, can be j,
              u, w, or a random choice of the 3

    Steps:
    1. In the message, the letters h, j, k, u, w, and y are replaced with ff,
       ii, qq, vv, xx, and zz respectively. If the letter is a capital, only
       the first letter in its pair is capitalized.
    2. The key and value list circles are aligned so the first letter of the
       message is in the key list and the pointer letter is directly under it.
       The pointer letter starts off the cipher.
       Key list = ABCDEFGILMNOPQRSTVXZ1234
       Value list = klnprtvz&xysomqihfdbaceg
    3. If the next letter is capital, the key list is rotated so the capital
       letter is above the pointer letter. The uppercase pointer letter is
       added to the cipher.
    4. If the next letter is lowercase, the value list character underneath the
       letter in the key list is added to the cipher.
    5. Steps 3-4 are repeated until message is enciphered.
    6. If there are any & symbols in the cipher, they are replaced with j, u,
       w, or a random choice of the three, depending on the ampRep argument.

    Returns cipher and if ampRep is random the random choice is returned.
    '''

    ## Variables
    # General
    cipher = ''
    valueList = 'klnprtvz&xysomqihfdbaceg'
    keyList = 'ABCDEFGILMNOPQRSTVXZ1234'
    cRand = ['rand', 'random']
    # Value letter and ampersand replacement
    valueLetter = pointerLetter.lower()
    ampRep = ampRep.lower()
    printValueLetter = valueLetter in cRand
    printAmpRep = ampRep in cRand
    if valueLetter in cRand: valueLetter = random.choice(valueList)
    if ampRep in cRand: ampRep = random.choice('juw')
    valueList = valueList.replace('&', ampRep)
    valueLetter = valueLetter.replace('&', ampRep)
    # Put appropriate characters in message
    message = [x for x in message if x in low + up + '1234']
    for letterInd, letter in enumerate(message):
        if letter.lower() in 'hjkuwy':
            for letter2, replacement in zip('hjkuwy', 'fiqvxz'):
                if letter.lower() == letter2:
                    message[letterInd] = replacement
                    message.insert(letterInd, eval('replacement'
                                   + ('', '.capitalize()')[letter in up]))
                    break
    # First value dictionary
    kInd = keyList.index(message[0].upper())
    keyList = keyList[kInd:] + keyList[:kInd]
    vInd = valueList.index(valueLetter)
    valueList = valueList[vInd:] + valueList[:vInd]
    valueDict = dict(zip(keyList, valueList))
    # Letter output
    valueLetter = (None, valueLetter)[printValueLetter]
    ampRep = (None, ampRep)[printAmpRep]

    ## Encipher
    for letter in message:
        # Translate letter
        if letter in up:
            # Capital letter reset
            kInd = keyList.index(letter)
            keyList = keyList[kInd:] + keyList[:kInd]
            valueDict = dict(zip(keyList, valueList))
        cipher += (valueDict[letter.upper()],
                   valueDict[letter.upper()].upper())[letter in up]

    ## Return cipher, valueLetter, and ampRep
    return (cipher, valueLetter, ampRep)

# Encipher method two
def encipher_alberti_method2(message, keyLetter='random',
                             pointerLetter='random', direction='random',
                             ampRep='random'):

    '''
    encipher_alberti_method2(message, keyLetter='random',
                             pointerLetter='random', direction='random',
                             ampRep='random')

    Two circles of letters are aligned and translated from the message to the
    cipher, and rotated according to the numbers 1-4 randomly placed every 1-4
    places in the message.

    Arguments:
    message -- Message being enciphered
    keyLetter -- Key list character lined up with the pointerLetter
    pointerLetter -- Value list character lined up with the keyLetter
    direction -- Direction of rotation of the key list (clockwise or
                 counterclockwise)
    ampRep -- Letter to replace each ampersand in the final cipher, can be j,
              u, w, or a random choice of the 3

    Steps:
    1. In the message, the letters h, j, k, u, w, and y are replaced with ff,
       ii, qq, vv, xx, and zz respectively. If the letter is a capital, only
       the first letter in its pair is capitalized.
    2. Every number in the list is turned into a Roman numeral with the
       function encipher_romannumeral so as to not interfere with the inserted
       numbers. If any number is too big (above 1 billion), None is
       returned.
    3. Numbers 1-4 are randomly inserted into the message every 1-4 steps.
       Each index and number is stored in an insertion list. For example, the
       message "happybirthday" could be "hap1py3birt1hda2y" with the
       insertion list [(3, 1), (6, 3), (11, 1), (15, 2), (17, 3)]. The last
       letter in the message cannot be a number, and is deleted if it is.
    4. The key and value lists are aligned so the keyLetter is above the
       pointerLetter.
    5. If the next letter is a letter, the value list character underneath the
       letter in the key list is added to the cipher.
    6. If the next letter is a number, the value list character underneath the
       number in the key list is added to the cipher, then the key list is
       rotated that number the direction specified in the argument direction.
    7. Steps 5-6 are repeated until message is enciphered.
    8. If there are any & symbols in the cipher, they are replaced with j, u,
       w, or a random choice of the three, depending on the ampRep argument.

    Returns cipher, insertion list, and if ampRep is random the random choice
    is returned.
    '''

    ## Variables
    # General
    insertionList, cipher = [], ''
    valueList = 'klnprtvz&xysomqihfdbaceg'
    keyList = 'ABCDEFGILMNOPQRSTVXZ1234'
    c = ['c', 'clockwise']
    cc = ['cc', 'counterclockwise']
    cRand = ['rand', 'random']
    # Value letter and ampersand replacement
    valueLetter = pointerLetter.lower()
    keyLetter = keyLetter.upper()
    direction = direction.lower()
    ampRep = ampRep.lower()
    printValueLetter = valueLetter in cRand
    printKeyLetter = keyLetter.lower() in cRand
    printDirection = direction in cRand
    printAmpRep = ampRep in cRand
    if valueLetter in cRand: valueLetter = random.choice(valueList)
    if keyLetter.lower() in cRand: keyLetter = random.choice(keyList)
    if direction in cRand: direction = random.choice(['clockwise',
                                                      'counterclockwise'])
    if ampRep in cRand: ampRep = random.choice('juw')
    valueList = valueList.replace('&', ampRep)
    valueLetter = valueLetter.replace('&', ampRep)
    # Put appropriate characters in message
    message = encipher_romannumeral(message)
    try: message = [x for x in message if x in low + up + '1234']
    except TypeError: return None, None, None
    for letterInd, letter in enumerate(message):
        if letter.lower() in 'hjkuwy':
            for letter2, replacement in zip('hjkuwy', 'fiqvxz'):
                if letter.lower() == letter2:
                    message[letterInd] = replacement
                    message.insert(letterInd, eval('replacement'
                                   + ('', '.capitalize()')[letter in up]))
                    break
    # First value dictionary
    kInd = keyList.index(keyLetter)
    keyList = keyList[kInd:] + keyList[:kInd]
    vInd = valueList.index(valueLetter)
    valueList = valueList[vInd:] + valueList[:vInd]
    valueDict = dict(zip(keyList, valueList))
    # Insertion list
    mesLen, p = len(message), 0
    while p < mesLen:
        placementSteps = (random.randint(2, 5), random.randint(1, 4))[p == 0]
        insertionList.append((p + placementSteps, random.randint(1, 4)))
        mesLen += 1
        p += placementSteps
    del insertionList[-1]
    # Letter output
    valueLetter = (None, valueLetter)[printValueLetter]
    keyLetter = (None, keyLetter)[printKeyLetter]
    ampRep = (None, ampRep)[printAmpRep]

    ## Encipher
    # Insert letters into message
    for index, number in insertionList: message.insert(index, str(number))
    if message[-1] in '1234': del message[-1]
    # Letter alteration
    for letter in message:
        # Rotation
        if letter in '1234':
            cipher += valueDict[letter]
            number = eval(('-', '')[direction in cc] + letter)
            keyList = keyList[number:] + keyList[:number]
            valueDict = dict(zip(keyList, valueList))
            continue
        # Letter
        cipher += (valueDict[letter.upper()],
                   valueDict[letter.upper()].upper())[letter in up]
    # Direction output
    direction = (None, direction)[printDirection]

    ## Return cipher, ampersand replacement, & insertion list
    return (cipher, valueLetter, keyLetter, direction, ampRep, insertionList)
