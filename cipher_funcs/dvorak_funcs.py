# Encipher
def encipher_dvorak(message, layers=1):

    '''
    encipher_dvorak(message, layers=1)

    The message is converted from the QWERTY keyboard to the Dvorak keyboard
    using the same key placements, done over the number of layers.

    Arguments:
    message -- Message being enciphered
    layers -- How many times the message is enciphered QWERTY to Dvorak

    Steps:
    1. Layers is put equal to layers modulo 210, as 210 is when the cipher
       repeats itself.
    2. Each message letter found in the QWERTY keyboard is set to the Dvorak
       keyboard, and put in the cipher.
    3. Step 2 is done as many times as there are layers, with each previous
       cipher as the new message.

    QWERTY keyboard:_______________
    │                              │
    │ ` 1 2 3 4 5 6 7 8 9 0 - =    │
    │    q w e r t y u i o p [ ] \\ │
    │     a s d f g h j k l ; '    │
    │      z x c v b n m , . /     │
    │______________________________│

    Dvorak keyboard:_______________
    │                              │
    │ ` 1 2 3 4 5 6 7 8 9 0 [ ]    │
    │    ' , . p y f g c r l / = \\ │
    │     a o e u i d h t n s -    │
    │      ; q j k x b m w v z     │
    │______________________________│

    Returns the cipher.
    '''

    ## Variables
    # Keysets
    qwerty = list('`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*'
                  + '()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? ')
    dvorak = list('`1234567890[]\',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz~!@#$%^&*'
                  + '(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ ')
    # Layers
    layers = int(layers) % 210
    if layers == 0: return message

    ## Encipher
    for _ in range(layers):
        cipher = ''
        for letter in message:
            if letter in qwerty:
                cipher += dvorak[qwerty.index(letter)]
            else:
                cipher += letter
        message = cipher

    ## Return cipher
    return cipher

# Decipher
def decipher_dvorak(cipher, layers=1):

    '''
    decipher_dvorak(cipher, layers=1)

    The cipher is converted from the Dvorak keyboard to the QWERTY keyboard
    using the same key placements, done over the number of layers.

    Arguments:
    cipher -- Cipher being deciphered
    layers -- How many times the cipher is deciphered Dvorak to QWERTY

    Steps:
    1. Layers is put equal to layers modulo 210, as 210 is when the message
       repeats itself.
    2. Each cipher letter found in the Dvorak keyboard is set to the QWERTY
       keyboard, and put in the message.
    3. Step 2 is done as many times as there are layers, with each previous
       message as the new cipher.

    Returns the message.
    '''

    ## Variables
    # Keysets
    dvorak = list('`1234567890[]\',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz~!@#$%^&*'
                  + '(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ ')
    qwerty = list('`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*'
                  + '()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? ')
    # Layers
    layers = int(layers) % 210
    if layers == 0: return cipher

    ## Decipher
    for _ in range(layers):
        message = ''
        for letter in cipher:
            if letter in dvorak:
                message += qwerty[dvorak.index(letter)]
            else:
                message += letter
        cipher = message

    ## Return message
    return message
