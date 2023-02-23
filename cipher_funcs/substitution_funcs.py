# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
from string import ascii_lowercase as low, ascii_uppercase as up, digits

# Encipher
def encipher_substitution(message, playfairKey, numbers=False):
    
    '''
    encipher_substitution(message, playfairKey, numbers=False)
    
    The letters/numbers from the message are substituted to another alphabet.
    
    Arguments:
    message -- Message being enciphered
    playfairKey -- Key put into the playfair_square function for the alphabet
                   that will align with the normal alphabet
    numbers -- False for numbers not to be part of the alphabets, True for
               numbers to be enciphered too
    
    Steps:
    1. A Playfair alphabet is retrieved from the function playfair_square
       with numbers as numbers and j as True.
    2. The normal alphabet is aligned with the Playfair alphabet.
    3. For every character in the message, the corresponding Playfair alphabet
       letter/number is put into the cipher. If the message character is not a
       letter, it is kept as is.
    
    Returns the cipher and the Playfair alphabet.
    '''
    
    ## Variables
    # General
    cipher = ''
    numbers = bool(numbers)
    # Playfair key
    sequence = ''.join(playfair_square(playfairKey, numbers, True))
    plDict = dict(zip((low, low + digits)[numbers], sequence))
    
    ## Encipher
    for letter in message:
        if letter.lower() in sequence:
            x = plDict[letter.lower()]
            cipher += (x.lower(), x.upper())[letter in up]
        else:
            cipher += letter
    
    ## Return cipher & sequence
    return cipher, sequence

# Decipher
def decipher_substitution(cipher, playfairKey, numbers=False):
    
    '''
    decipher_substitution(cipher, playfairKey, numbers=False)
    
    The letters/numbers from the cipher are substituted from another alphabet.
    
    Arguments:
    cipher -- Cipher being deciphered
    playfairKey -- Key put into the playfair_square function for the alphabet
                   that will align with the normal alphabet
    numbers -- False for numbers not to be part of the alphabets, True for
               numbers to be enciphered too
    
    Steps:
    1. A Playfair alphabet is retrieved from the function playfair_square
       with numbers as numbers and j as True.
    2. The Playfair alphabet is aligned with the normal alphabet.
    3. For every character in the cipher, the normal alphabet letter/number 
       that corresponds to the Playfair alphabet letter/number is put into the
       message. If the cipher character is not a letter, it is kept as is.
    
    Returns the message and the Playfair alphabet.
    '''
    
    ## Variables
    # General
    message = ''
    numbers = bool(numbers)
    # Playfair key
    sequence = ''.join(playfair_square(playfairKey, numbers, True))
    plDict = dict(zip(sequence, (low, low + digits)[numbers]))
    
    ## Encipher
    for letter in cipher:
        if letter.lower() in sequence:
            x = plDict[letter.lower()]
            message += (x.lower(), x.upper())[letter in up]
        else:
            message += letter
    
    ## Return message & sequence
    return message, sequence