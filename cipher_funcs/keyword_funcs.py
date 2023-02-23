# Import
try:
    from playfair_funcs import playfair_square
except ModuleNotFoundError:
    from .playfair_funcs import playfair_square
from string import ascii_lowercase as low, digits

# Encipher
def encipher_keyword(message, key, numbers=False):
    
    '''
    encipher_keyword(message, key, numbers=False)
    
    The alphabet and the key alphabet (put through the playfair_square 
    function) are lined up and the message letters are ciphered through.
    
    Arguments:
    message -- Message being enciphered
    key -- Key put into the playfair_square function for the second alphabet
    numbers -- False for the alphabets to include only letters, True to
               include numbers in the alphabets and accept them for the key
    
    Steps:
    1. The key is put through the playfair_square function, creating an
       alphabet without repeating letters and numbers if numbers is True.
    2. The normal alphabet and the key alphabet are lined up. Every message
       letter is input through the normal alphabet and its corresponding key 
       alphabet character is output into the cipher. If the character is not 
       in the alphabet, it is copied into the cipher.
    
    Returns the cipher.
    '''
    
    ## Variables
    # General
    cipher = ''
    message = message.lower()
    numbers = bool(numbers)
    # Dictionary
    key = ''.join(playfair_square(key, numbers, True))
    dictionary = dict(zip((low, low + digits)[numbers], key))
    
    ## Encipher
    for letter in message:
        try: cipher += dictionary[letter]
        except KeyError: cipher += letter
    
    ## Return cipher & key
    return cipher, key

# Decipher
def decipher_keyword(cipher, key, numbers=False):
    
    '''
    decipher_keyword(cipher, key, numbers=False)
    
    The key alphabet (put through the playfair_square function) and the 
    normal alphabet are lined up and the cipher letters are ciphered through.
    
    Arguments:
    cipher -- Cipher being enciphered
    key -- Key put into the playfair_square function for the second alphabet
    numbers -- False for the alphabets to include only letters, True to
               include numbers in the alphabets and accept them for the key
    
    Steps:
    1. The key is put through the playfair_square function, creating an
       alphabet without repeating letters and numbers if numbers is True.
    2. The key alphabet and the normal alphabet are lined up. Every cipher
       letter is input through the normal alphabet and its corresponding key 
       alphabet character is output into the message. If the character is not 
       in the alphabet, it is copied into the message.
    
    Returns the message.
    '''
    
    ## Variables
    # General
    message = ''
    cipher = cipher.lower()
    numbers = bool(numbers)
    # Dictionary
    key = playfair_square(key, numbers, True)
    dictionary = dict(zip(key, (low, low + digits)[numbers]))
    
    ## Decipher
    for letter in cipher:
        try: message += dictionary[letter]
        except KeyError: message += letter
    
    ## Return message
    return message