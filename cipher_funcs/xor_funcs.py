# To binary
def to_bin(inp, binary):
    # Integer
    if isinstance(inp, int) and not binary:
        inp = ''.join(f'{int(x):08b}' for x in str(inp))
    elif isinstance(inp, int):
        inp = str(inp)
        while int(len(inp) / 8) != len(inp) / 8:
            inp = '0' + inp
    # String or list of characters
    elif isinstance(inp, str):
        inp = ''.join(f'{ord(x):08b}' for x in inp)
    # List of integers
    elif binary:
        inp = ''.join(f'{x:08}' for x in inp)
    else:
        inp = [abs(x) for x in inp if abs(x) < 256]
        inp = ''.join(f'{int(x):08b}' for x in inp)
    return inp

# Encipher
def encipher_xor(message, key, mesBin=False, keyBin=False):

    '''
    encipher_xor(message, key, mesBin=False, keyBin=False)

    The message and key are converted to binary and put through the XOR
    operation.

    Arguments:
    message -- Message being enciphered
    key -- Key compared with the message
    mesBin -- True for message numbers to be read as binary, otherwise False
    keyBin -- True for key numbers to be read as binary, otherwise False

    Steps:
    1. The message is converted to binary through:
       a. If the message is a decimal integer, each digit is converted to an
          8-digit binary number.
       b. If the message is a string or list of strings, each character is
          converted to a number through ord(x), then converted to 8-digit
          binary numbers.
       c. If the message is a list of integers, the ones less than 256 are
          converted to 8-digit binary numbers.
    2. Step 1 is done to the key, and the key is repeated over itself until
       its length is >= the message length.
    3. A XOR operation is done to each character lined up in the message and
       key. If the two numbers are the same, the resulting number is 0. If
       they are different, the resulting number is 1.
       M   K   C
       0 │ 0 │ 0
       0 │ 1 │ 1
       1 │ 0 │ 1
       1 │ 1 │ 0
    4. The binary sequence is taken, a decimal integer sequence is taken from
       each 8 digits, and each integer is turned into a character through
       chr(x).

    Returns the binary cipher, integer cipher, and character cipher.
    '''

    ## Variables
    # Message
    message = to_bin(message, mesBin)
    # Key
    key = to_bin(key, keyBin)
    while len(key) < len(message): key += key

    ## Encipher
    # Binary cipher
    cipher = ''.join(str(int(x) ^ int(y)) for x, y in zip(message, key))
    binCipher = cipher
    # Integer cipher
    cipher = [int(cipher[x:x + 8], 2) for x in range(0, len(cipher), 8)]
    intCipher = cipher
    # Character cipher
    cipher = ''.join(chr(x) for x in cipher)

    ## Return ciphers
    return binCipher, intCipher, cipher

# Decipher
def decipher_xor(cipher, key, ciphBin=False, keyBin=False):

    '''
    decipher_xor(cipher, key, ciphBin=False, keyBin=False)

    The cipher and key are converted to binary and put through the XOR
    operation.

    Arguments:
    cipher -- Cipher being deciphered
    key -- Key compared with the cipher
    ciphBin -- True for cipher numbers to be read as binary, otherwise False
    keyBin -- True for key numbers to be read as binary, otherwise False

    Steps:
    1. The cipher and key are put through the encipher_xor function and the
       binary, integer, and character messages are obtained.

    Returns the binary message, integer message, and character message.
    '''

    ## Decipher
    binMessage, intMessage, message = encipher_xor(cipher, key, ciphBin, keyBin)

    ## Return messages
    return binMessage, intMessage, message
