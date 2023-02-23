# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
try:
    from polybiussquare_funcs import encipher_polybiussquare
except ModuleNotFoundError:
    from .polybiussquare_funcs import encipher_polybiussquare

# Encipher
def encipher_nihilist(message, key, playfairKey=None,
                      numbers=False, listReturn=False):

    '''
    encipher_nihilist(message, key, playfairKey=None,
                      numbers=False, listReturn=False)

    The message and key are put through the encipher_polybiussquare function
    and the numbers are added together.

    Arguments:
    message -- Message being enciphered
    key -- Keyword made to match the message length
    playfairKey -- Key for the playfair_square function for the sequence of
                   letters in the grid
    numbers -- False for 5x5 square without j, True for 6x6 square with digits
    listReturn -- False to return one string of numbers, True to return list

    Steps:
    1. The key is repeated until its length is >= the message length.
    2. The message and key are put through the encipher_polybiussquare
       function, and 2-number pairs are extracted.
    3. The message and key numbers are added together in sequence.
    4. If listReturn is False, the numbers are put together in a string. If it
       is True, the numbers are kept in a list.

    Returns the cipher and the playfair alphabet from encipher_polybiussquare.
    '''

    ## Variables
    # General
    numbers = bool(numbers)
    listReturn = bool(listReturn)
    playfairKey = ''.join(playfair_square(playfairKey, numbers, numbers))
    # Message
    message, sequence = encipher_polybiussquare(message, playfairKey, numbers)
    message = [message[x:x + 2] for x in range(0, len(message), 2)]
    # Key
    while len(key) < len(message): key += key
    key, sequence = encipher_polybiussquare(key, playfairKey, numbers)
    key = [key[x:x + 2] for x in range(0, len(key), 2)]

    ## Encipher
    cipher = list(zip(message, key))
    for ind, tup in enumerate(cipher):
        cipher[ind] = str(int(tup[0]) + int(tup[1]))

    ## Return cipher & sequence
    return (''.join(cipher), [int(x) for x in cipher])[listReturn], sequence
