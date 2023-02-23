# Import
from math import sqrt, ceil
from string import ascii_lowercase as low, digits

# Reduced list
def reduce(x):
    if isinstance(x, list) and isinstance(x[0], str):
        x = ''.join(x)
    if isinstance(x, str):
        x = ''.join(y for y in x.lower() if y in low)
    if isinstance(x, int):
        return [int(y) for y in str(x)]
    elif isinstance(x, str):
        return [low.index(y) for y in x]
    else:
        return x

# Encipher
def encipher_hill(message, key):

    '''
    encipher_hill(message, key)

    Perfect square matrices are created from the message and key, then each is
    put through calculations to get a number from each that is made to
    represent a letter/number for the cipher.

    Arguments:
    message -- Message being enciphered
    key -- Letters or numbers for the key matrix

    Steps:
    1. The message is converted to a message matrix through:
       a. Its letters are converted to numbers as a-z = 0-25 and converted to
          a number list.
       b. The closest number >= the message length's square root is n.
       c. The message is repeated until its length is n^2.
       d. Every n numbers in the message are put as a list into its matrix.
    2. The key is converted to a key matrix through:
       a. Its letters are converted to numbers as a-z = 0-25 and converted to
          a number list.
       b. The key is repeated until its length is n^2.
       c. Every n numbers in the key are put as a list into its matrix.
    3. The key matrix is lined up with the message matrix. For example:
       key=[[9 8 7]  message=[[1 2 3]
            [6 5 4]           [4 5 6]
            [3 2 1]]          [7 8 9]]
    4. Each key sublist is lined up with the first message sublist and the
       values are independently multiplied then added together. For example:
        [9 8  7]      [6 5  4]      [3 2 1]
       *[1 2  3]     *[1 2  3]     *[1 2 3]
         9+16+21 = 46  6+10+12 = 28  3+4+3 = 10 (First 3 values = 46, 28, 10)
    5. Step 4 is repeated n times so there are a resulting n*n values.
       In this example, those would be: 46, 28, 10, 118, 73, 28, 190, 118, 46
    6. Each value is modded by 26.
       In this example, those would be: 20, 2, 10, 14, 21, 2, 8, 14, 20
    7. The numbers are converted to letters.

    Returns the number list cipher and the letter cipher.
    '''

    ## Variables
    # General
    cipher, mtrix, ktrix = [], [], []
    # Message
    message = reduce(message)
    if len(message) == 0: raise ValueError
    n = ceil(sqrt(len((str(key), key)[isinstance(key, list)])))
    while len(message) < n ** 2:
        message += message
    for x in range(n):
        mtrix.append(message[:n])
        del message[:n]
    # Key
    key = reduce(key)
    if len(key) == 0: raise ValueError
    while len(key) < n ** 2:
        key += key
    for x in range(n):
        ktrix.append(key[:n])
        del key[:n]

    ## Encipher
    # Calculate numbers
    for m in mtrix:
        for k in ktrix:
            x = 0
            for num in range(len(k)):
                x += m[num] * k[num]
            cipher.append(x % 26)
    numCipher = cipher[:]
    # Turn numbers to letters
    for xInd, x in enumerate(cipher):
        if x in range(26): cipher[xInd] = low[x]
        else: cipher[xInd] = str(x - 26)
    cipher = ''.join(cipher)

    ## Return numCipher and cipher
    return numCipher, cipher
