# Import
try:
    from morse_funcs import encipher_morse, decipher_morse
except ModuleNotFoundError:
    from .morse_funcs import encipher_morse, decipher_morse
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square

# Encipher
def encipher_fractionatedmorse(message, playfairKey=None):
    
    '''
    encipher_fractionatedmorse(message, playfairKey=None)
    
    The message is translated to morse, then translated back to letters
    through a table determined by the Playfair key.
    
    Arguments:
    message -- Message being enciphered
    playfairKey -- Key for the alphabet dictionary
    
    Steps:
    1. The message is converted to morse code through the encipher_morse
       function. The letter separator is 'x', the word separator is 'xx', and
       the other arguments are default.
    2. The message is then split into 3s. If the last triplet doesn't have 3
       characters, 'x's are added to it.
       For example, if the message is 'Attack at dawn', the new message
       would be '.-x -x- x.- x-. -.x -.- xx. -x- xx- ..x .-x .-- x-.'
    3. The Playfair key is put through the playfair_square function and is set
       to a table of '.'s, '-'s, and 'x's. With the key zebras, the table is:
       zebrascdfghijklmnopqtuvwxy
       .........---------xxxxxxxx
       ...---xxx...---xxx...---xx
       .-x.-x.-x.-x.-x.-x.-x.-x.-
       The series of symbols always looks the same.
    4. Each triplet of message symbols is translated to a letter and the
       resulting cipher is found. In this case, the cipher is 'snquihxnybsau'.
    
    Returns the cipher, Playfair sequence, and the table.
    '''
    
    ## Variables
    # General
    cipher = ''
    # Message
    message = encipher_morse(message, 'x', 'xx')
    message = [message[x:x+3] for x in range(0, len(message), 3)]
    while len(message[-1]) < 3: message[-1] += 'x'
    # Playfair key
    playfairKey = ''.join(playfair_square(playfairKey, j=True))
    key = list(playfairKey)
    ind = 0
    for f in '.-x':
        for s in '.-x':
            for t in '.-x':
                key[ind] = (key[ind], f + s + t)
                ind += 1
                if ind == 26: break
            if ind == 26: break
        if ind == 26: break
    
    ## Encipher
    for x in message:
        for y in key:
            if x == y[1]:
                cipher += y[0]
    
    ## Return cipher and keys
    return cipher, playfairKey, key

# Decipher
def decipher_fractionatedmorse(cipher, playfairKey):
    
    '''
    decipher_fractionatedmorse(cipher, playfairKey)
    
    The cipher is converted to morse through the Playfair key, then the morse
    is translated back to text.
    
    Arguments:
    cipher -- Cipher being deciphered
    playfairKey -- Key for the alphabet dictionary
    
    Steps:
    1. The Playfair key is put through the playfair_square function and is set
       to a table of '.'s, '-'s, and 'x's. With the key zebras, the table is:
       zebrascdfghijklmnopqtuvwxy
       .........---------xxxxxxxx
       ...---xxx...---xxx...---xx
       .-x.-x.-x.-x.-x.-x.-x.-x.-
       The series of symbols always looks the same.
    2. Each letter of the cipher is translated to '.'s, '-'s, and 'x's based
       on the key table. In this instance, if the cipher is 'snquihxnybsau',
       the symbols put together are '.-x-x-x.-x-.-.x-.-xx.-x- xx-..x.-x.--x-.'
    3. The morse code is translated back to letters through the
       decipher_morse function with the letter separator as 'x', the word
       separator as 'xx', and the other arguments are default.
       In this instance, the message is 'attack at dawn'.
    
    Returns the message, Playfair sequence, and the table.
    '''
    
    ## Variables
    # General
    message = ''
    # Playfair key
    playfairKey = ''.join(playfair_square(playfairKey, j=True))
    key = list(playfairKey)
    ind = 0
    for f in '.-x':
        for s in '.-x':
            for t in '.-x':
                key[ind] = (key[ind], f + s + t)
                ind += 1
                if ind == 26: break
            if ind == 26: break
        if ind == 26: break
    
    ## Decipher
    for x in cipher:
        for y in key:
            if x == y[0]:
                message += y[1]
    message = decipher_morse(message.strip('x'), 'x', 'xx')[0]
    
    ## Return message and keys
    return message, playfairKey, key
