# Import
try:
    from columnartransposition_funcs import encipher_columnartransposition
except ModuleNotFoundError:
    from .columnartransposition_funcs import encipher_columnartransposition

# Encipher
def encipher_doubletransposition(message, key1, key2=None, 
                                 nulls=False, keepNonLetters=True):
    
    '''
    encipher_doubletransposition(message, key1, key2=None, 
                                 nulls=False, keepNonLetters=True)
    
    The message is put through the columnar transposition cipher twice.
    
    Arguments:
    message -- Message being enciphered
    key1 -- First columnar transposition key
    key2 -- Second columnar transpotision key, key1 if None
    nulls -- Equal to the nulls argument in encipher_columnartransposition
    keepNonLetters -- Equal to the keepNonLetters argument in
                      encipher_columnartransposition
    
    Steps:
    1. The arguments are put into encipher_columnartransposition with key1.
       This is the first cipher.
    2. The arguments are put into encipher_columnartransposition with key2 and
       the first cipher. This is the final cipher.
    
    Returns the final cipher.
    '''
    
    ## Variables
    if not key2: key2 = key1
    nulls = bool(nulls)
    keepNonLetters = bool(keepNonLetters)
    
    ## Encipher
    cipher = encipher_columnartransposition(
                 encipher_columnartransposition(
                                                message, key1, 
                                                nulls, keepNonLetters
                                               ), 
                                            key2, nulls, keepNonLetters
                                           )
    
    ## Return cipher
    return cipher
