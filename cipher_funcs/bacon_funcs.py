# Import
try:
    from randomsentence_funcs import random_sentence
except ModuleNotFoundError:
    from .randomsentence_funcs import random_sentence
import random
from string import ascii_lowercase as low, ascii_uppercase as up

# Encipher
def encipher_bacon(message):

    '''
    encipher_bacon(message)

    Converts letters to binary, generates a random message, then changes its
    letters to the binary code using uppercase and lowercase letters.

    Arguments:
    message -- Message being enciphered

    Steps:
    1. Each letter is converted to a 5 letter binary string, with a as 0 and
       z as 25.
       For example, "bar" would be 00001 00000 10001.
    2. Random sentences are generated with the random_sentence function.
    3. In order of the binary sequence, the sentence letters are set
       lowercase for 0, uppercase for 1. When there are no more numbers to
       assign, the 0 or 1 is randomly chosen.

    Returns sentences.
    '''

    ## Variables
    # General
    binaryMessage = ''
    # Message
    message = [x for x in message.lower() if x in low]
    if message == []:
        return print('Needs letters.')
    # Letter to binary
    letterToBinary = list(range(26))
    for dInd, dec in enumerate(letterToBinary):
        letterToBinary[dInd] = f'{dec:05b}'
    letterToBinary = dict(zip(low, letterToBinary))
    # Binary message and random sentences
    for letter in message:
        binaryMessage += letterToBinary[letter]
    sentences = list(random_sentence(len(binaryMessage), True))
    binaryMessage = iter(binaryMessage)

    ## Encipher
    for letInd, letter in enumerate(sentences):
        if letter in low + up:
            try:
                n = next(binaryMessage)
            except StopIteration:
                n = random.choice((0, 0, 0, 0, 1, 1, 1, 1, 1))
            sentences[letInd] = (letter.upper(), letter.lower())[int(n) == 0]
    cipher = ''.join(sentences)

    ## Return cipher
    return cipher

# Decipher
def decipher_bacon(cipher):

    '''
    decipher_bacon(cipher)

    Converts letters to 0s and 1s based on their case, then turns the binary
    to letters.

    Arguments:
    cipher -- Sentences being deciphered

    Steps:
    1. Each letter in the sentences is converted to a 0 if it's lowercase and 1
       if it's uppercase.
    2. Every 5 numbers are converted to decimal, then to letters, with 0 as a
       and 25 as z.

    Returns message.
    '''

    ## Variables
    # General
    message = ''
    binaryCipher = []
    # Cipher
    cipher = [x for x in cipher if x in low + up]
    while len(cipher) % 5 != 0: del cipher[-1]
    if cipher == []:
        return print('Cipher must have at least five letters.')
    # Binary to letter
    binaryToLetter = list(range(26))
    for dInd, dec in enumerate(binaryToLetter):
        binaryToLetter[dInd] = f'{dec:05b}'
    binaryToLetter = dict(zip(binaryToLetter, low))
    # Binary cipher
    for letter in cipher:
        binaryCipher.append((1, 0)[letter in low])

    ## Decipher
    for y in range(len(cipher) // 5):
        number = ''.join(str(x) for x in binaryCipher[:5])
        try: message += binaryToLetter[number]
        except KeyError: break
        del binaryCipher[:5]

    ## Return message
    if bool(message):
        return message
    else:
        return print('\nNot a bacon cipher...\n')
