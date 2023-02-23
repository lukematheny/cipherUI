# Import
from string import ascii_lowercase as low, ascii_uppercase as up

# Encipher
def encipher_porta(message, key, alphNum=1, kInNonL=False):

    '''
    encipher_porta(message, key, alphNum=1, kInNonL=False)

    A message and key are put through 1 of 2 tabula rectas.

    Arguments:
    message -- Message being enciphered
    key -- Key made to match the message length by repeating itself
    alphNum -- 1 or 2, specifies which tabula recta is used
    kInNonL -- False for the key to only apply to letters, otherwise True

    Steps:
    1. If kInNonL is False, all non-letters from the message are documented
       and deleted. All non-letters in the key are taken out.
    2. The key is added to itself until its length equals the message length,
       and the key and message are lined up.
    3. Each letter pair from the message and key are put into 1 of 2 alphabets
       with the message letter on top and the key letter on the side.
                      Alphabet 1                  Alphabet 2
              abcdefghijklmnopqrstuvwxyz  abcdefghijklmnopqrstuvwxyz
       (a,b)  NOPQRSTUVWXYZABCDEFGHIJKLM  NOPQRSTUVWXYZABCDEFGHIJKLM
       (c,d)  ZNOPQRSTUVWXYBCDEFGHIJKLMA  OPQRSTUVWXYZNMABCDEFGHIJKL
       (e,f)  YZNOPQRSTUVWXCDEFGHIJKLMAB  PQRSTUVWXYZNOLMABCDEFGHIJK
       (g,h)  XYZNOPQRSTUVWDEFGHIJKLMABC  QRSTUVWXYZNOPKLMABCDEFGHIJ
       (i,j)  WXYZNOPQRSTUVEFGHIJKLMABCD  RSTUVWXYZNOPQJKLMABCDEFGHI
       (k,l)  VWXYZNOPQRSTUFGHIJKLMABCDE  STUVWXYZNOPQRIJKLMABCDEFGH
       (m,n)  UVWXYZNOPQRSTGHIJKLMABCDEF  TUVWXYZNOPQRSHIJKLMABCDEFG
       (o,p)  TUVWXYZNOPQRSHIJKLMABCDEFG  UVWXYZNOPQRSTGHIJKLMABCDEF
       (q,r)  STUVWXYZNOPQRIJKLMABCDEFGH  VWXYZNOPQRSTUFGHIJKLMABCDE
       (s,t)  RSTUVWXYZNOPQJKLMABCDEFGHI  WXYZNOPQRSTUVEFGHIJKLMABCD
       (u,v)  QRSTUVWXYZNOPKLMABCDEFGHIJ  XYZNOPQRSTUVWDEFGHIJKLMABC
       (w,x)  PQRSTUVWXYZNOLMABCDEFGHIJK  YZNOPQRSTUVWXCDEFGHIJKLMAB
       (y,z)  OPQRSTUVWXYZNMABCDEFGHIJKL  ZNOPQRSTUVWXYBCDEFGHIJKLMA
       Note: The key letters refer to only the alphabet chosen, not to each
             alphabet exclusively.
    4. Their intersections are put into the cipher. If kInNonL is True, a key
       letter is skipped when there is a non-letter in the message.

    Returns the cipher.
    '''

    ## Variables
    # General
    cipher, nonL = '', []
    kInNonL = bool(kInNonL)
    alphNum = alphNum == 2
    # Alphabets
    AB1 = ['nopqrstuvwxyzabcdefghijklm', 'znopqrstuvwxybcdefghijklma',
           'yznopqrstuvwxcdefghijklmab', 'xyznopqrstuvwdefghijklmabc',
           'wxyznopqrstuvefghijklmabcd', 'vwxyznopqrstufghijklmabcde',
           'uvwxyznopqrstghijklmabcdef', 'tuvwxyznopqrshijklmabcdefg',
           'stuvwxyznopqrijklmabcdefgh', 'rstuvwxyznopqjklmabcdefghi',
           'qrstuvwxyznopklmabcdefghij', 'pqrstuvwxyznolmabcdefghijk',
           'opqrstuvwxyznmabcdefghijkl']
    AB2 = ['nopqrstuvwxyzabcdefghijklm', 'opqrstuvwxyznmabcdefghijkl',
           'pqrstuvwxyznolmabcdefghijk', 'qrstuvwxyznopklmabcdefghij',
           'rstuvwxyznopqjklmabcdefghi', 'stuvwxyznopqrijklmabcdefgh',
           'tuvwxyznopqrshijklmabcdefg', 'uvwxyznopqrstghijklmabcdef',
           'vwxyznopqrstufghijklmabcde', 'wxyznopqrstuvefghijklmabcd',
           'xyznopqrstuvwdefghijklmabc', 'yznopqrstuvwxcdefghijklmab',
           'znopqrstuvwxybcdefghijklma']
    # Document and delete non-letters
    if not kInNonL:
        for cInd, char in enumerate(message):
            if char not in low + up:
                nonL.append((cInd, char))
        message = [x for x in message if x in low + up]
    # Key
    key = [x.lower() for x in key if x.lower() in low]
    while len(key) < len(message): key += key

    ## Encipher
    # Translate
    for m, k in zip(message, key):
        if m in low + up:
            alphStr = low.index(k.lower()) // 2
            c = (AB1, AB2)[alphNum][alphStr][low.index(m.lower())]
            cipher += (c, c.upper())[m in up]
        elif kInNonL:
            cipher += m
    # Insert non-letters
    if not kInNonL:
        cipher = list(cipher)
        for cInd, char in nonL: cipher.insert(cInd, char)
        cipher = ''.join(cipher)

    ## Return cipher
    return cipher

# Decipher
def decipher_porta(cipher, key, alphNum=1, kInNonL=False):

    '''
    decipher_porta(cipher, key, alphNum=1, kInNonL=False)

    A cipher is reverse translated through 1 of 2 tabula rectas.

    Arguments:
    cipher -- Cipher being deciphered
    key -- Key made to match the cipher length by repeating itself
    alphNum -- 1 or 2, specifies which tabula recta is used
    kInNonL -- False for the key to only apply to letters, otherwise True

    Steps:
    1. If kInNonL is False, all non-letters from the message are documented
       and deleted. All non-letters in the key are taken out.
    2. The key is added to itself until its length equals the message length,
       and the key and message are lined up.
    3. Each letter pair from the cipher and key are taken and interpreted from
       one of two tabula rectas (as documented in encipher_porta).
    4. The key letter specifies the row, and the cipher letter in that row
       shows which letter is put into the message. If kInNonL is True, a key
       letter is skipped when there is a non-letter in the message.

    Returns the message.
    '''

    ## Variables
    # General
    message, nonL = '', []
    kInNonL = bool(kInNonL)
    alphNum = alphNum == 2
    # Alphabets
    AB1 = ['nopqrstuvwxyzabcdefghijklm', 'znopqrstuvwxybcdefghijklma',
           'yznopqrstuvwxcdefghijklmab', 'xyznopqrstuvwdefghijklmabc',
           'wxyznopqrstuvefghijklmabcd', 'vwxyznopqrstufghijklmabcde',
           'uvwxyznopqrstghijklmabcdef', 'tuvwxyznopqrshijklmabcdefg',
           'stuvwxyznopqrijklmabcdefgh', 'rstuvwxyznopqjklmabcdefghi',
           'qrstuvwxyznopklmabcdefghij', 'pqrstuvwxyznolmabcdefghijk',
           'opqrstuvwxyznmabcdefghijkl']
    AB2 = ['nopqrstuvwxyzabcdefghijklm', 'opqrstuvwxyznmabcdefghijkl',
           'pqrstuvwxyznolmabcdefghijk', 'qrstuvwxyznopklmabcdefghij',
           'rstuvwxyznopqjklmabcdefghi', 'stuvwxyznopqrijklmabcdefgh',
           'tuvwxyznopqrshijklmabcdefg', 'uvwxyznopqrstghijklmabcdef',
           'vwxyznopqrstufghijklmabcde', 'wxyznopqrstuvefghijklmabcd',
           'xyznopqrstuvwdefghijklmabc', 'yznopqrstuvwxcdefghijklmab',
           'znopqrstuvwxybcdefghijklma']
    # Document and delete non-letters
    if not kInNonL:
        for cInd, char in enumerate(cipher):
            if char not in low + up:
                nonL.append((cInd, char))
        cipher = [x for x in cipher if x in low + up]
    # Key
    key = [x.lower() for x in key if x.lower() in low]
    while len(key) < len(cipher): key += key

    ## Decipher
    # Translate
    for c, k in zip(cipher, key):
        if c in low + up:
            alphStr = low.index(k.lower()) // 2
            m = low[(AB1, AB2)[alphNum][alphStr].index(c.lower())]
            message += (m, m.upper())[c in up]
        elif kInNonL:
            message += c
    # Insert non-letters
    if not kInNonL:
        message = list(message)
        for cInd, char in nonL: message.insert(cInd, char)
        message = ''.join(message)

    ## Return message
    return message
