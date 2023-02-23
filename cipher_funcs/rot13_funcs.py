# Import
from string import ascii_lowercase as low, ascii_uppercase as up

# Encipher
def encipher_rot13(message):
    
    '''
    encipher_rot13(message)
    
    Replaces each letter with the 13th letter after it, wrapping to front.
    
    Arguments:
    message -- Message being enciphered
    
    Steps:
    1. For each letter in the message, the 13th letter after it is put into
       the cipher. If the encipherment reaches the end of the alphabet, it is
       wrapped around to the front.
    
    Returns cipher.
    '''
    
    ## Variables
    cipher = ''
    
    ## Encipher
    for m in message:
        x = (65, 97)[m in low]
        cipher += (m, chr((ord(m) + 13 - x) % 26 + x))[m in low + up]
    
    ## Return cipher
    return cipher

# Decipher
def decipher_rot13(cipher):
    
    '''
    decipher_rot13(cipher)
    
    Replaces each letter with the 13th letter after it, wrapping to front.
    
    Arguments:
    cipher -- Cipher being deciphered
    
    Steps:
    1. The cipher is put through the function encipher_rot13 for the message.
    
    Returns message.
    '''
    
    ## Decipher
    message = encipher_rot13(cipher)
    
    ## Return message
    return message