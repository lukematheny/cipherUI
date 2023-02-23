# Import
try:
    import numpy
except ImportError:
    print('Install numpy for the Playfair cipher.')
from string import ascii_lowercase as low, digits
from random import shuffle, choice

# Playfair square
def playfair_square(key=None, numbers=False, j=False, alphabet=None):

    '''
    playfair_square(key=None, numbers=False, j=False, alphabet=None)

    Generates a 25, 26, 35, or 36 letter sequence of letters and numbers based
    on the arguments.

    Arguments:
    key -- Determines which letters come first in the sequence, None to
           generate a randomly shuffled sequence
    numbers -- False to have no numbers in the sequence, otherwise True
    j -- False to have no j in the sequence, best for numbers to be False as
         it creates a 5*5 square (25 characters long), True to have a j in
         the sequence, best for numbers to be True as it creates a 6*6 square
         (36 characters long)

    Steps:
    1. An alphabet is generated with/without numbers and a j based on the
       arguments numbers and j.
    2. If key is None, the alphabet is shuffled and returned as a list.
    3. A sequence list is created, and the key is iterated over, with any
       letters not in the sequence added to the sequence.
    4. The alphabet is then iterated over, with any letters not in the
       sequence added to it, to fill in all 25, 26, 35, or 36 spaces.

    Returns the sequence in list form.
    '''

    ## Variables
    # General
    sequence = []
    numbers = bool(numbers)
    if j == None: j = numbers
    j = bool(j)
    # Alphabet
    if alphabet == None:
        alphabet = (list(low), list(low + digits))[numbers]
        if not j: del alphabet[9]
    else:
        alphabet = list(alphabet)
    # Key
    if key == None:
        shuffle(alphabet)
        return alphabet
    if not j: key = key.lower().replace('j', 'i')
    key = [x for x in key.lower() if x in alphabet]

    ## Make sequence
    # Insert key
    for x in key:
        if x not in sequence: sequence.append(x)
    # Insert alphabet
    for x in alphabet:
        if x not in sequence: sequence.append(x)

    ## Return sequence
    return sequence

# Encipher
def encipher_playfair(message, key=None, numbers=False):

    '''
    encipher_playfair(message, key=None, numbers=False)

    A Playfair square is generated from the key, and each pair of message
    letters is transformed to new positions on the square.

    Arguments:
    message -- Message being enciphered
    key -- Playfair key making an alphabet with the key at the start and no
           repeating letters
    numbers -- False to have a Playfair square that is 5x5 with no j, True for
               a 6x6 Playfair square with all letters and numbers

    Steps:
    1. The message is split into pairs. If the last pair is incomplete, a
       random letter is added to the end.
    2. The key is made into a Playfair square through the playfair_square
       function, 5x5 if numbers is False or 6x6 if numbers is True.
       For example, if the key is 'qwerty' and numbers is False, the Playfair
       square would look like:
       q w e r t
       y a b c d
       f g h i k
       l m n o p
       s u v x z
    3. Each message pair is plotted (with i as j if numbers is False). If they
       have the same row, the right of each letter in order is added to the
       cipher, wrapping left if needed. If the two letters have the same
       column, the bottom of each letter in order is added to the cipher,
       wrapping up if needed. If the letters have the same position, they are
       translated right.
       In this example, 'et' would be 'rq' and 'ri' would be 'co'.
    4. If the pair has neither the same row or column, a box is created around
       the letters and the 2 new corner letters are plotted in order of
       horizontality with the original letters.
       In this example, 'cm' would be 'ao' and 'uk' would be 'zg'.
    5. The new letters are strung together.

    Returns the cipher and the Playfair sequence.
    '''

    ## Variables
    # General
    cipher = []
    numbers = bool(numbers)
    n = (5, 6)[numbers]
    # Message
    message = (message.lower().replace('j', 'i'), message.lower())[numbers]
    message = [x for x in message if x in (low, low + digits)[numbers]]
    message = [message[x:x + 2] for x in range(0, len(message), 2)]
    if len(message[-1]) == 1: message[-1].append(choice(low))
    # Key array
    sequence = playfair_square(key, numbers, numbers)
    key = numpy.array([sequence[x:x + n] for x in range(0, len(sequence), n)])
    sequence = ''.join(sequence)

    ## Encipher
    for letter1, letter2 in message:
        first, second = numpy.where(key==letter1), numpy.where(key==letter2)
        x1, y1, x2, y2 = first[0], first[1], second[0], second[1]
        # Shift right
        if x1 == x2:
            y1 += 1; y2 += 1
            if y1 == n: y1 = 0
            if y2 == n: y2 = 0
            cipher += list(key[x1, y1])
            cipher += list(key[x2, y2])
        # Shift down
        elif y1 == y2:
            x1 += 1; x2 += 1
            if x1 == n: x1 = 0
            if x2 == n: x2 = 0
            cipher += list(key[x1, y1])
            cipher += list(key[x2, y2])
        # Intersections
        else:
            cipher += list(key[x1, y2])
            cipher += list(key[x2, y1])
    cipher = ''.join(cipher)

    ## Return cipher, sequence, & key
    return cipher, sequence, key

# Decipher
def decipher_playfair(cipher, key, numbers=False):

    '''
    decipher_playfair(cipher, key, numbers=False)

    A Playfair square is generated from the key, and each pair of cipher
    letters is transformed to new positions on the square.

    Arguments:
    cipher -- Cipher being deciphered
    key -- Playfair key making an alphabet with the key at the start and no
           repeating letters
    numbers -- False to have a Playfair square that is 5x5 with no j, True for
               a 6x6 Playfair square with all letters and numbers

    Steps:
    1. The cipher is split into pairs. If the last pair is incomplete, a
       random letter is added to the end.
    2. The key is made into a Playfair square through the playfair_square
       function, 5x5 if numbers is False or 6x6 if numbers is True.
       For example, if the key is 'qwerty' and numbers is False, the Playfair
       square would look like:
       q w e r t
       y a b c d
       f g h i k
       l m n o p
       s u v x z
    3. Each cipher pair is plotted (with i as j if numbers is False). If they
       have the same row, the left of each letter in order is added to the
       message, wrapping right if needed. If the two letters have the same
       column, the top of each letter in order is added to the message,
       wrapping down if needed. If the letters have the same position, they
       are translated left.
       In this example, 'et' would be 'wr' and 'ri' would be 'xc'.
    4. If the pair has neither the same row or column, a box is created around
       the letters and the 2 new corner letters are plotted in order of
       horizontality with the original letters.
       In this example, 'cm' would be 'ao' and 'uk' would be 'zg'.
    5. The new letters are strung together.

    Returns the message and the Playfair sequence.
    '''

    ## Variables
    # General
    message = []
    numbers = bool(numbers)
    n = (5, 6)[numbers]
    # Cipher
    cipher = (cipher.lower().replace('j', 'i'), cipher.lower())[numbers]
    cipher = [x for x in cipher if x in (low, low + digits)[numbers]]
    cipher = [cipher[x:x + 2] for x in range(0, len(cipher), 2)]
    if len(cipher[-1]) == 1: cipher[-1].append(choice(low))
    # Key array
    sequence = playfair_square(key, numbers, numbers)
    key = numpy.array([sequence[x:x + n] for x in range(0, len(sequence), n)])
    sequence = ''.join(sequence)

    ## Decipher
    for letter1, letter2 in cipher:
        first, second = numpy.where(key==letter1), numpy.where(key==letter2)
        x1, y1, x2, y2 = first[0], first[1], second[0], second[1]
        # Shift left
        if x1 == x2:
            y1 -= 1; y2 -= 1
            if y1 == -1: y1 = n - 1
            if y2 == -1: y2 = n - 1
            message += list(key[x1, y1])
            message += list(key[x2, y2])
        # Shift up
        elif y1 == y2:
            x1 -= 1; x2 -= 1
            if x1 == -1: x1 = n - 1
            if x2 == -1: x2 = n - 1
            message += list(key[x1, y1])
            message += list(key[x2, y2])
        # Intersections
        else:
            message += list(key[x1, y2])
            message += list(key[x2, y1])
    message = ''.join(message)

    ## Return message, sequence, & key
    return message, sequence, key
