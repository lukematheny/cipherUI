# Import
from string import ascii_lowercase as low, ascii_uppercase as up

# Encipher
def encipher_vigenere(message, key, form='v', kInNonL=False):

    '''
    encipher_vigenere(message, key, form='v', kInNonL=False)

    The letters from the key and the message or letters from the message are
    aligned to each other, their alphabet indices are added or subtracted from
    each other based on the form argument, then the cipher letters correspond
    to each alphabet letter.

    Arguments:
    message -- Message being enciphered
    key -- Key made to match the message length by repeating itself
    form -- V (Vigenere), B (Beaufort), or G (German), always reads
            as V as long as it isn't B or G
    kInNonL -- False for the key to only apply to letters, otherwise True

    Steps:
    1. If kInNonL is False, all non-letters from the message are documented
       and deleted. All non-letters in the key are taken out.
    2. The key is added to itself until its length equals the message length,
       and the key and message are lined up.
    3. The alphabet index of the key letter and the alphabet index of the
       message letter lined up with it are taken.
    4. If the form is V, the indices are added. If the form is B, the message
       index is subtracted from the key index. If the form is G, the key index
       is subtracted from the message index. The resulting index is put modulo
       to 26 to put it between 0 and 25 with 0 as A and 25 as Z.
    5. Each letter made forms the cipher. Steps 3-4 are done until the entire
       message is enciphered.

    Returns the cipher.
    '''

    ## Variables
    # General
    cipher, nonL = '', []
    kInNonL = bool(kInNonL)
    # Document and delete non-letters
    if not kInNonL:
        for cInd, c in enumerate(message):
            if c not in low + up:
                nonL.append((cInd, c))
        message = [x for x in message if x in low + up]
    # Key
    key = [x.lower() for x in key if x.lower() in low]
    if len(key) == 0: raise ValueError
    while len(key) < len(message): key += key

    ## Encipher
    # Translate
    for m, k in zip(message, key):
        if m in low + up:
            if form.lower() == 'b':
                letter = low[(low.index(k) - low.index(m.lower())) % 26]
            elif form.lower() == 'g':
                letter = low[(low.index(m.lower()) - low.index(k)) % 26]
            else:
                letter = low[(low.index(k) + low.index(m.lower())) % 26]
            cipher += (letter.upper(), letter)[m in low]
        elif kInNonL:
            cipher += m
    # Insert non-letters
    if not kInNonL:
        cipher = list(cipher)
        for cInd, c in nonL: cipher.insert(cInd, c)
        cipher = ''.join(cipher)

    ## Return cipher
    return cipher
