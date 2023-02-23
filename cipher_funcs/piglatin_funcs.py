# Import
from string import ascii_lowercase as low, ascii_uppercase as up, \
ascii_letters as let

# Variables
owelsvay = 'aeiouy'
onsonantscay = 'bcdfghjklmnpqrstvwxz'

# Starts with a consonant
def cStart(word):
    '''For words that start with a consonant.'''
    start, end = '', ''
    while word[0] not in low: start += word[0]; word = word[1:]
    while word[-1] not in low: end += word[-1]; word = word[:-1]
    if word[-1] == 'x': word = word[:-1] + 'cks'
    if any(x in owelsvay for x in word[1:]):
        for x in word[1:]:
            if x in owelsvay: ind = word.index(x); break
        word = word[ind:] + word[:ind]
    return start + word + 'ay' + end[::-1]

# Starts with a vowel
def vStart(word, asC=True):
    '''For words that start with a vowel.'''
    start, end = '', ''
    while word[0] not in low: start += word[0]; word = word[1:]
    while word[-1] not in low: end += word[-1]; word = word[:-1]
    if word[-1] == 'x': word = word[:-1] + 'cks'
    for x in word[::-1]:
        if x in owelsvay: ind = word.rindex(x); break
    if not any(x in onsonantscay for x in word[:ind]): asC = False
    if asC:
        for x in word:
            if x in onsonantscay: ind = word.index(x); break
        for xInd, x in enumerate(word[ind:]):
            if x in owelsvay: ind = xInd + 1; break
        word = word[ind:] + word[:ind]
    return start + word + ('way', 'ay')[asC] + end[::-1]

# Encipher
def encipher_piglatin(message, vStartAsC=True):

    '''
    encipher_piglatin(message, vStartAsC=True)

    Each word in the message is repositioned with vowels at the start and 'ay'
    at the end.

    Arguments:
    message -- Message being enciphered
    vStartAsC -- Refers to a word starting with a vowel. True to interpret the
                 first vowel(s) as consonants, False to add 'way' to the end

    Steps:
    1. All words of the message are split into a list, separated by spaces.
    2. Capital words and uppercase words are documented by their indices.
    3. Any word without letters is deleted (to be inserted later).
    4. Each word goes through this process:
       a. The start and end of the word are documented if they aren't letters.
       b. If the last letter is x, it is changed to 'cks'.
       c. If it starts with a consonant:
          i. The front consonant(s) are moved to the back if there are vowels.
          ii. The letters 'ay' are added to the end.
       d. If it starts with a vowel:
          i. It is checked if there are vowels separated by consonants.
          ii. If step i is true and vStartAsC is True, the first vowel(s) are
              interpreted as consonants and step c is applied.
              For example:
                If vStartAsC is True, envelope would be 'elopeenvay'.
                If vStartAsC is False, envelope would be 'envelopeway'.
                Regardless of what vStartAsC is, end will be 'endway' because
                there is only 1 group of vowels.
          iii. Otherwise, 'way' is added to the end.
       e. If there are starts and ends saved from step a, they are added.
    5. The words deleted in step 3 are reinserted.
    6. Each documented capital/uppercase index is made that way in the cipher.

    Returns cipher.'''

    ## Variables
    # General
    cipher = []
    vStartAsC = bool(vStartAsC)
    # Message
    message = [x for x in message.split(' ') if bool(x)]
    # Document capitalization
    cap, upp = [], []
    for ind, word in enumerate(message):
        wordLets = [x for x in word if x in let]
        if bool(wordLets):
            if all(x in up for x in wordLets): upp.append(ind)
            elif wordLets[0] in up: cap.append(ind)
    # Deleted strings
    delStrings = []
    for xInd, x in reversed(list(enumerate(message))):
        if all(y not in let for y in x):
            delStrings.append((xInd, x))
            del message[xInd]

    ## Encipher
    # Convert words
    for word in message:
        word = word.lower()
        for letter in word:
            if letter in onsonantscay + 'y': c = True; break
            elif letter in owelsvay: c = False; break
        if c: cipher.append(cStart(word))
        else: cipher.append(vStart(word, vStartAsC))
    # Place deleted strings
    for ind, word in reversed(delStrings):
        cipher.insert(ind, word)
    # Put capitalization
    for ind in upp:
        cipher[ind] = cipher[ind].upper()
    for ind in cap:
        word = list(cipher[ind])
        for x in word:
            if x in low: word[word.index(x)] = x.upper(); break
        cipher[ind] = ''.join(word)
    cipher = ' '.join(cipher)

    ## Return cipher
    return cipher
