# Import
try:
    from polybiussquare_funcs import encipher_polybiussquare, \
    decipher_polybiussquare
except ModuleNotFoundError:
    from .polybiussquare_funcs import encipher_polybiussquare, \
    decipher_polybiussquare
from string import ascii_lowercase as low, ascii_uppercase as up, digits

# Encipher
def encipher_bifid(message, playfairKey=None, numbers=False):
    
    '''
    encipher_bifid(message, playfairKey=None, numbers=False)
    
    The message is enciphered to Polybius square coordinates, rearranged, then
    deciphered from coordinates to a cipher using the same alphabet.
    
    Arguments:
    message -- Message being enciphered
    playfairKey -- Playfair key for the Polybius squares
    numbers -- True for 6x6 Playfair square, False for 5x5 Playfair square
    
    Steps:
    1. The message is enciphered using the encipher_polybiussquare function, 
       using the Playfair key and numbers arguments.
    2. Line up the coordinates like:
       0 2 4 6 8
       1 3 5 7 9
    3. The numbers are read off by row, resulting in:
       0246813579
    4. The new coordinates are deciphered by the decipher_polybiussquare 
       function, using the same Playfair key and numbers arguments.
    
    Returns cipher and Playfair alphabet.
    '''
    
    ## Variables
    # Numbers
    numbers = bool(numbers)
    # Convert message to coordinates
    coords, alphabet = encipher_polybiussquare(message, playfairKey, numbers) 
    coords = list(coords)
    
    ## Encipher
    # Columnated coordinates
    for nInd, num in enumerate(coords[1:len(coords)], 1):
        coords.append(num)
        del coords[nInd]
    coords = ''.join(coords)
    # Convert revised coordinates to cipher
    cipher, alphabet = decipher_polybiussquare(coords, alphabet, numbers)
    
    ## Return cipher and alphabet
    return cipher, alphabet

# Decipher
def decipher_bifid(cipher, playfairKey=None, numbers=False):
    
    '''
    decipher_bifid(cipher, playfairKey=None, numbers=False)
    
    The cipher is enciphered to Polybius square coordinates, rearranged, then
    deciphered from coordinates to a cipher using the same alphabet.
    
    Arguments:
    cipher -- Cipher being deciphered
    playfairKey -- Playfair key for the Polybius squares
    numbers -- True for 6x6 Playfair square, False for 5x5 Playfair square
    
    Steps:
    1. The message is enciphered using the encipher_polybiussquare function,
       using the Playfair key and numbers arguments.
    2. The coordinates are lined up with the first half on the left and second
       half on the right, both vertically:
       0 5
       1 6
       2 7
       3 8
       4 9
    3. The numbers are read off by row, resulting in:
       0516273849
    4. The new coordinates are deciphered by the decipher_polybiussquare
       function, using the same Playfair key and numbers arguments.
    
    Returns message and Playfair alphabet.
    '''
    
    ## Variables
    # Numbers
    numbers = bool(numbers)
    # Convert cipher to coordinates
    coords, alphabet = encipher_polybiussquare(cipher, playfairKey, numbers)
    coords, coordLen = list(coords), len(coords)
    
    ## Decipher
    # Decolumnated coordinates
    for num1, num2 in zip(coords[:coordLen // 2], coords[coordLen // 2:]):
        coords.append(num1 + num2)
    coords = ''.join(coords[coordLen:])
    # Convert revised coordinates to message
    message, alphabet = decipher_polybiussquare(coords, alphabet, numbers)
    
    ## Return message and alphabet
    return message, alphabet
