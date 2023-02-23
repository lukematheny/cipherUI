# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
from string import ascii_lowercase as low, digits

# Encipher
def encipher_chaocipher(message, plainPlayfair=None, 
                        ciphPlayfair=None, numbers=False):
    
    '''
    encipher_chaocipher(message, plainPlayfair=None, 
                        ciphPlayfair=None, numbers=False)
    
    The message is translated from plaintext alphabet to the ciphertext 
    alphabet. After each letter is translated, the plaintext and ciphertext
    alphabets are altered.
    
    Arguments:
    message -- Message being enciphered
    plainPlayfair -- Plaintext Playfair key
    ciphPlayfair -- Ciphertext Playfair key
    numbers -- True for digits in playfair keys, False for no digits
    
    Steps:
    1. The plaintext and ciphertext Playfair alphabets are generated and 
       lined up like:
       Plaintext:  abcdefghijklmnopqrstuvwxyz
       Ciphertext: abcdefghijklmnopqrstuvwxyz
    2. The first message letter is translated from the plaintext to ciphertext
       alphabet downward. "B" would translate to b in this example.
    3. In the plaintext alphabet, the message letter and any before it are
       shifted to the back, then the third character is shifted to the 14th
       slot, like:
       cdfghijklmnopeqrstuvwxyzab
       abcdefghijklmnopqrstuvwxyz
    4. In the ciphertext alphabet, any letters before the translated message
       letter are shifted to the back, then the second characer is shifted to
       the 14th slot, like:
       cdfghijklmnopeqrstuvwxyzab
       bdefghijklmnocpqrstuvwxyza
    5. Steps 2-4 are repeated for each letter.
    
    Returns cipher and original plaintext and ciphertext alphabets.
    '''
    
    ## Variables
    # General
    cipher = ''
    numbers = bool(numbers)
    # Message
    alphabet = (low, low + digits)[numbers]
    message = [x for x in message.lower() if x in alphabet]
    # Alphabets
    plainAB = playfair_square(plainPlayfair, numbers, True)
    plaintext = ''.join(plainAB)
    ciphAB = playfair_square(ciphPlayfair, numbers, True)
    ciphertext = ''.join(ciphAB)
    
    ## Encipher
    for letter in message:
        # Append to cipher
        index = plainAB.index(letter)
        cipher += ciphAB[index]
        # Permute plaintext alphabet
        plainAB[:] = plainAB[index + 1:] + plainAB[:index + 1]
        plainAB.insert(14, plainAB[2])
        plainAB.remove(plainAB[2])
        # Permute ciphertext alphabet
        ciphAB[:] = ciphAB[index:] + ciphAB[:index]
        ciphAB.insert(14, ciphAB[1])
        ciphAB.remove(ciphAB[1])
    
    ## Return cipher & alphabets
    return cipher, plaintext, ciphertext
