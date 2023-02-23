# Import
try:
    from cld2 import detect
except ImportError:
    print('Install cld2-cffi (Compact Language Detector) '
          + 'to help detect English.')
    detect = None
try:
    from vigenere_funcs import encipher_vigenere
except ModuleNotFoundError:
    from .vigenere_funcs import encipher_vigenere
from string import ascii_lowercase as low, digits

# Encipher
def encipher_trithemius(message, start=0, ascend=True, kInNonL=False):
    
    '''
    encipher_trithemius(message, start=0, ascend=True, kInNonL=False)
    
    Message letters are shifted based on starting point, shifting positive or
    negative one extra for each new letter.
    
    Arguments:
    message -- Message being enciphered
    start -- Starting number of the sequence
    ascend -- True for the sequence to go up from the starting number, False
              for it to go down
    kInNonL -- False for the key to only apply to letters, otherwise True
    
    Steps:
    1. A sequence is made, the length of the message, starting with the start
       number, and going up or down based on the ascend argument.
    2. Every number in the sequence is set modulo 26 so they are all 0 to 25.
       Then they are changed from numbers to letters with 0-25 as a-z.
    3. The message, sequence and kInNonL are put through the Vigenere cipher
       with form as 'vigenere'.
    
    Returns the cipher.
    '''
    
    ## Variables
    # General
    ascend = bool(ascend)
    start = round(start)
    # Message
    length = len(message)
    # Sequence
    sequence = list(range(start, (start - length, start + length)[ascend],
                          (-1, 1)[ascend]))
    sequence = [low[x % 26] for x in sequence]
    
    ## Encipher
    cipher = encipher_vigenere(message, sequence, 'v', kInNonL)
    
    ## Return cipher
    return cipher

# Decipher
def decipher_trithemius(cipher, start=None, ascend=None, kInNonL=False):
    
    '''
    decipher_trithemius(cipher, start=None, ascend=None, kInNonL=False)
    
    Cipher letters are shifted based on starting point, shifting positive or
    negative one extra for each new letter.
    
    Arguments:
    cipher -- Cipher being enciphered
    start -- Starting number of the sequence, None if unknown
    ascend -- True if the sequence went up from the starting number, False
              if it went down, None if unknown
    kInNonL -- False for the key to only apply to letters, otherwise True
    
    Steps:
    1. If the start or ascend is known:
       a. start is made negative.
       b. ascend is made opposite.
    2. If the start and ascend are both known, the new start and ascend are
       put back into the encipher_trithemius function.
    3. If the either start or ascend is unknown, all possibilities are
       documented by being put back into the encipher function.
    4. Potential English messages are put into a second list if compact
       language detector 2 is installed.
    
    Returns message, messages, and English messages if applicable.
    '''
    
    ## Variables
    messages, engMessages = [], []
    if start != None: start = -round(start)
    if ascend != None: ascend = not bool(ascend)
    
    ## Decipher
    # Unknown start or ascend
    if None in (start, ascend):
        if start == None:
            # Unknown start and ascend
            if ascend == None:
                for x in range(26):
                    y = -x % 26
                    a = encipher_trithemius(cipher, y, False, kInNonL)
                    b = encipher_trithemius(cipher, y, True, kInNonL)
                    messages += [a, b]
                    if detect:
                        for message in (a, b):
                            if detect(message).details[0][1] == 'en':
                                engMessages.append((message, f'{x:02}',
                                                    ('↑', '↓')[message == b]))
            # Unknown start
            else:
                for x in range(26):
                    y = -x % 26
                    message = encipher_trithemius(cipher, y, ascend, kInNonL)
                    messages.append(message)
                    if detect and detect(message).details[0][1] == 'en':
                        engMessages.append((message, f'{x:02}',
                                            ('↑', '↓')[ascend]))
        # Unknown ascend
        else:
            for x in (False, True):
                message = encipher_trithemius(cipher, start, x, kInNonL)
                messages.append(message)
                if detect and detect(message).details[0][1] == 'en':
                    engMessages.append((message, start, ('↑', '↓')[x]))
    # Known start and ascend
    else:
        messages = encipher_trithemius(cipher, start, ascend, kInNonL)
    
    ## Return message
    return ((messages, None), (messages, engMessages))[bool(engMessages)]
