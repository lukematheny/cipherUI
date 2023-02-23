# Import
from string import ascii_lowercase as low

# Check if coprime to 26
def coprime26(number):
    '''Returns True if number is a coprime of 26, False if not.'''
    return (number % 2 == 0 or number % 13 == 0)

# Encipher
def encipher_affine(message, a, b):

    '''
    encipher_affine(message, a, b)

    Letters are translated to their numeric equivalents, multiplied by a,
    added to b, made modulo to 26, and translated back to letters.

    Arguments:
    message -- Message being enciphered
    a -- Multiplier for the first set of numbers, must be coprime to 26
    b -- Added to numbers after multiplied by a

    Steps:
    1. Letters are translated to their numeric equivalents with A as 0, B as
       1... Z as 25.
       For example, "bar" would be 1 0 17.
    2. Each number is multiplied by a.
       For example, if a = 5, 1 0 17 would be 5 0 85.
    3. Each number is added to b.
       For example, if b = 8, 5 0 85 would be 13 8 93.
    4. Each number is made modulo to 26, to get all numbers below 26. Modulo
       means that the largest multiple of 26 that's less than the number is
       subtracted from the number.
       For example, 13 8 93 would be 13 8 15.
    5. Numbers are translated to their letter equivalents with the previous
       guide.
       For example, 13 8 15 would result in "nip" as the cipher.

    Returns the cipher.
    '''

    ## Variables
    # General
    message = [x for x in message.lower() if x in low]
    enumLow = list(enumerate(list(low)))
    numList, cipher = [], ''

    ## Encipher
    # Make number list
    for let in message:
        for number, letter in enumLow:
            if let == letter:
                numList.append((a * number + b) % 26)
                break
    # Translate to letters
    for num in numList:
        for number, letter in enumLow:
            if num == number:
                cipher += letter

    ## Return cipher
    return cipher

# Decipher
def decipher_affine(cipher, a, b):

    '''
    decipher_affine(cipher, a, b)

    A's inverse is found, letters are translated to their number equivalents,
    b is subtracted from them, multiplied by a^-1, made modulo to 26, and
    translated back to letters.

    Arguments:
    cipher -- Cipher being deciphered
    a -- Determines a's inverse (a^-1), cannot be coprime of 26
    b -- Subtracted from numbers before multiplied by a^-1

    Steps:
    1. A^-1 is whichever number multiplied by a, modulo 26 equals 1. A^-1
       will be coprime to 26.
       For example, if a = 5, a^-1 = 21.
    2. Letters are translated to their number equivalents with A as 0, B as
       1... Z as 25.
       For example, "nip" would be 13 8 15.
    3. B is subtracted from each number.
       For example, if b = 8, 13 8 15 would be 5 0 7.
    4. Each number is multiplied by a^-1.
       For example, with a^-1 as 21, 5 0 7 is 105 0 147.
    5. Each number is made modulo to 26, to get all numbers below 26. Modulo
       means that the largest multiple of 26 that's less than the number is
       subtracted from the number.
       For example, 105 0 147 is 1 0 17.
    6. Numbers are translated to their letter equivalents with the previous
       guide.
       For example, 1 0 17 would result in "bar" as the message.

    Returns the message.
    '''

    ## Variables
    # General
    cipher = [x for x in cipher.lower() if x in low]
    enumLow = list(enumerate(list(low)))
    numList, message = [], ''
    # Find a^-1
    for x in range(1, 26, 2):
        if a * x % 26 == 1:
            a_1 = x
            break

    ## Decipher
    # Make number list
    for let in cipher:
        for number, letter in enumLow:
            if let == letter:
                numList.append(a_1 * (number - b) % 26)
                break
    # Translate to letters
    for num in numList:
        for number, letter in enumLow:
            if num == number:
                message += letter

    ## Return message
    return message
