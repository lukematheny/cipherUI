# Import
try:
    from cld2 import detect
except ImportError:
    print('Install cld2-cffi (Compact Language Detector) '
          + 'to help detect English.')
    detect = None
from string import ascii_lowercase as low, ascii_letters as let

# Encipher
def encipher_caesar(message, shift=-3):

    '''
    encipher_caesar(message, shift=-3)

    Sets 2 alphabets to translate the first to the second, with the second
    offset by the shift (right for positive shift, left for negative shift).

    Arguments:
    message -- Message being enciphered
    shift -- Degree of rotation of the second alphabet (where the resulting
             letters come from)

    Steps:
    1. Two alphabets are aligned in a circle, with each letter corresponding
       to its equivalent.
    2. One alphabet is shifted right once for each shift value, and left for
       each negative shift value. This is the second alphabet, with the
       other being the first.
    3. Each message letter is put into the first alphabet and whichever letter
       corresponds to it in the second alphabet becomes the cipher.

    Returns the cipher.
    '''

    ## Variables
    cipher = ''
    shift = int((shift % -26, shift % 26)[shift >= 0])

    ## Encipher
    for m in message:
        x = (65, 97)[m in low]
        cipher += (m, chr((ord(m) + shift - x) % 26 + x))[m in let]

    ## Return cipher
    return cipher

# Decipher
def decipher_caesar(cipher, shift=None):

    '''
    decipher_caesar(cipher, shift=None)

    Sets 2 alphabets to translate the first to the second, with the second
    offset by the shift (right for positive shift, left for negative shift).

    Arguments:
    cipher -- Cipher being deciphered
    shift -- None if shift is unknown, number for degree of rotation of the
             second alphabet (where the cipher letters are put to translate)

    Steps:
    1. Two alphabets are aligned in a circle, with each letter corresponding
       to its equivalent.
    2. One alphabet is shifted right once for each shift value, and left for
       each negative shift value. This is the first alphabet, with the
       other being the second.
    3. Each cipher letter is put into the first alphabet and whichever letter
       corresponds to it in the second alphabet becomes the message.
    4. If the shift is None, steps 2-3 are done 24 more times with shifts
       1-25. If cld2-cffi is installed, each message will be detected for
       English words.

    Returns the message if shift is known, returns the 25 messages if the
    shift is unknown and any English messages if they are detected.
    '''

    ## Variables
    messages, engMessages = [], []

    ## Decipher
    # Unknown shift
    if shift == None:
        for shift in range(1, 26):
            message = ''
            for c in cipher:
                x = (65, 97)[c in low]
                message += (c, chr((ord(c) + shift - x) % 26 + x))[c in let]
            messages.append(message)
            if detect and detect(message).details[0][1] == 'en':
                engMessages.append((message, -shift % 26))
    # Known shift
    else:
        messages = ''
        shift = int((shift % -26, shift % 26)[shift >= 0])
        for c in cipher:
            x = (65, 97)[c in low]
            messages += (c, chr((ord(c) - shift - x) % 26 + x))[c in let]

    ## Return messages and engMessages
    return ((messages, None), (messages, engMessages))[bool(engMessages)]
