# Import
try:
    from caesarbox_funcs import zipall
except ModuleNotFoundError:
    from .caesarbox_funcs import zipall
from string import ascii_letters as let, digits

# Encipher
def encipher_railfence(message, rails=3, keepNonLetNum=True):

    '''
    encipher_railfence(message, rails=3, keepNonLetNum=True)

    The message is put on a series of rails and is read off by row.

    Arguments:
    message -- Message being enciphered
    rails -- Number of rails the message lies on, can be negative or positive
    keepNonLetNum -- True to include all message letters, False to only
                     include message letters and numbers

    Steps:
    1. If keepNonLetNum is False, non-letters/non-numbers are taken out of the
       message.
    2. Rails are created, the number decided by the rails argument.
    3. If the rails argument is positive, the message starts from the top
       rail. If it is negative, it starts from the bottom rail.
    4. The message is spread across the rails going right by one and switching
       rails by one each time.
       For example, if rails is 3, onlyLetNum is True, and the message is
       'happy birthday', the rails would look like:
       h - - - y - - - t - - - y
       - a - p - b - r - h - a -
       - - p - - - i - - - d - -
    5. The message is read off by rows, top to bottom for the cipher.
       In this example, the cipher is 'hytyapbrhapid'.

    Returns the cipher.
    '''

    ## Variables
    # General
    keepNonLetNum = bool(keepNonLetNum)
    rails = int(rails)
    if rails == 0: rails = 3
    if not keepNonLetNum: message = [x for x in message if x in let + digits]
    # Cycle
    cyclePeak = abs(rails)
    cycleLen = 2 * cyclePeak - 2
    cycle = list(range(1, cycleLen + 1))
    cycle = [(x, 2 * cyclePeak - x)[x > cyclePeak] for x in cycle]
    # Start from bottom rail if rails is negative
    if rails < 0:
        average = (min(cycle) + max(cycle)) / 2
        cycle = [2 * average - x for x in cycle]

    ## Encipher
    # Converge cycle repititions and message
    message = list(enumerate(message))
    message = [list(zip(cycle, message[x:x + cycleLen]))
               for x in range(0, len(message), cycleLen)]
    # Sort message
    message = sorted([y for x in message for y in x])
    cipher = ''.join(x[1][1] for x in message)

    ## Return cipher
    return cipher

# Decipher
def decipher_railfence(cipher, rails=3):

    '''
    decipher_railfence(cipher, rails=3)

    The cipher is put on a series of rails and is read off by column.

    Arguments:
    cipher -- Cipher being deciphered
    rails -- Number of rails the cipher lies on, can be negative or positive

    Steps:
    1. Groups of variables are taken, such as the cycle length, number of
       cycles, and the remainder.
       For example, with the cipher as 'hytyapdrhapid' and rails as 3, the
       cycle length would be 4 [2 * |rails| - 2], meaning there are 3 whole
       cycles and a remainder of 1 letter (13 letters / cycle length).
    2. The cipher is separated into groups, which represent which rail they
       belong to. Middle groups are paired.
       In this example, the cipher is separated into 'hyty apdrha pid'.
       a. hytyapbrhapid
       b. hyt yap brh api d (4 steps, 3 cycles each with 1 remainder)
       c. hyty apb rha pid (remainder distributed to front)
       d. hyty apbrha pid (middle groups joined because they share rails)
    3. The middle group(s) are divided and sent to the back.
       In this example, the cipher is separated into 'hyty abh pid pra'.
       a. hyty apbrha pid
       b. hyty a b h  pid ▲
                p r a ────┘
       c. hyty abh pid pra
    4. The strings are lined up vertically and read off by column.
       In this case, the message is 'happy birthday'.
       h y t y ┐
       a b h   │
       p i d   │
       p r a ──┴ is read off by column.

    Returns the message.
    '''

    ## Variables
    # General
    rails = int(rails)
    if rails == 0: rails = 3
    if abs(rails) >= len(cipher): return (cipher, cipher[::-1])[rails < 0]
    cipher = list(cipher)
    # |rails| < cipher length < 2 * |rails| - 2
    if abs(rails) < len(cipher) < 2 * abs(rails) - 2:
        ## Variables
        extra = ''
        r = len(cipher) - abs(rails)
        ## Decipher
        if rails > 0:
            for x in range(-2, -2 * r - 1, -2): extra += cipher[x]
            for x in reversed(range(-2, -2 * r - 1, -2)): del cipher[x]
            message = ''.join(cipher) + extra
        else:
            for x in range(2, 2 * r + 1, 2): extra += cipher[x]
            for x in reversed(range(2, 2 * r + 1, 2)): del cipher[x]
            message = ''.join(cipher[::-1]) + extra
        ## Return message
        return message
    # Cycle variables
    cyclePeak = abs(rails) - 1
    cycleLen = 2 * cyclePeak
    fullCycles = int(len(cipher) / cycleLen)
    r = round(cycleLen * ((len(cipher) / cycleLen) - fullCycles))
    # Cycle
    cycle = []
    for x in range(cyclePeak + 1):  # Assign rails to groups of letters
        nums = list(str(x) * fullCycles)
        cycle += (nums, nums * 2)[0 < x < cyclePeak]
    for x in range(r):  # Insert remainders to end
        if x > cyclePeak: x = cycleLen - x
        cycle.append(str(x))
    cycle = [int(x) for x in sorted(cycle)]  # Sort back remainders
    if rails < 0: cycle = list(reversed(cycle))  # Reverse if negative rails
    for ind, x in enumerate(cycle):  # Alternate middle number groups
        if 0 < x < cyclePeak and cycle[ind - 1] == x:
            cycle[ind] = cycleLen - x

    ## Decipher
    # Sort cycle into cipher
    cipher = sorted(list(zip(cycle, list(range(len(cipher))), cipher)))
    cipher = [(x, z) for x, y, z in cipher]
    # Sort by rail
    message = [[] for x in range(cycleLen)]
    for num, x in cipher: message[num].append(x)
    # Zip lists
    message = ''.join(zipall(message))

    ## Return message
    return message
