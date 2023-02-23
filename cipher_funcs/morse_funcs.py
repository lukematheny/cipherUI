# -*- coding: utf-8 -*-

# Encipher
def encipher_morse(message, letSep=' ', wordSep=' / ',
                   çTR=False, ðHR=False, èIT=False):

    '''
    encipher_morse(message, letSep=' ', wordSep=' / ',
                   çTR=False, ðHR=False, èIT=False)

    Translates letters to morse code.

    Arguments:
    message -- Message being enciphered
    letSep -- String to separate letters in cipher
    wordSep -- String to separate words in cipher
    çTR -- False to translate ç to its normal format (-.-..), True to
           translate ç to its Turkish format (.-.-)
    ðHR -- False to translate ð to its normal format (..--.), True to
           translate ð to its Croatian format (..-..)
    èIT -- False to translate è to its normal format (.-..-), True to
           translate è to its Italian format (..-..)

    Steps:
    1. The message is separated into words by spaces. If any letters aren't in
       the morse dictionary, they are taken out.
    2. Each letter is translated based on the morse dictionary. Arguments çTR,
       ðHR, and èIT are considered. Morse dictionary:
       a .-      ã .--.-  á .--.-   å .--.-  à .--.-   â .--.-  ä .-.-
       ą .-.-    æ .-.-   b -...    c -.-.   ç -.-..   ć -.-..  ĉ -.-..
       č -.--.   d -..    ð ..--.   e .      è .-..-   ë ..-..  ę ..-..
       é ..-..   ê -..-.  f ..-.    g --.    ğ --.-.   ĝ --.-.  h ....
       ĥ ----    i ..     ï -..--   ì .---.  j .---    ĵ .---.  k -.-
       l .-..    ł .-..-  m --      n -.     ń --.--   ñ --.--  o ---
       ó ---.    ò ---.   ö ---.    ô ---.   ø ---.    p .--.   q --.-
       r .-.     s ...    ś ...-... ş .--..  ș ----    š ----   ŝ ...-.
       ß ...--.. t -      þ .--..   u ..-    ü ..--    ù ..--   ŭ ..--
       û ..--    v ...-   w .--     x -..-   y -.--    z --..   ž --..-
       ź --..-   ż --..-. 1 .----   2 ..---  3 ...--   4 ....-  5 .....
       6 -....   7 --...  8 ---..   9 ----.  0 -----   , --..-- . .-.-.-
       ; -.-.-   : ---... / -..-.   - -....- ' .----.  " .-..-. ? ..--..
       ¿ ..-.-   ! -.-.-- ¡ --...-  @ .--.-. $ ...-..- & .-...  ( -.--.
       ) -.--.-  _ ..--.- = -...-   + .-.-.  error ........
    3. Each letter is separated in a string by letSep. Each word is separated
       in the string by wordSep.

    Returns the cipher.
    '''

    ## Variables
    # General
    cipher = []
    çTR, ðHR, èIT = bool(çTR), bool(ðHR), bool(èIT)
    # Dictionary
    morse = {'a': '.-',      'ã': '.--.-',  'á': '.--.-',  'å': '.--.-',
             'à': '.--.-',   'â': '.--.-',  'ä': '.-.-',   'ą': '.-.-',
             'æ': '.-.-',    'b': '-...',   'c': '-.-.',   'ç': '-.-..',
             'ć': '-.-..',   'ĉ': '-.-..',  'č': '-.--.',  'd': '-..',
             'ð': '..--.',   'e': '.',      'è': '.-..-',  'ë': '..-..',
             'ę': '..-..',   'é': '..-..',  'ê': '-..-.',  'f': '..-.',
             'g': '--.',     'ğ': '--.-.',  'ĝ': '--.-.',  'h': '....',
             'ĥ': '----',    'i': '..',     'ï': '-..--',  'ì': '.---.',
             'j': '.---',    'ĵ': '.---.',  'k': '-.-',    'l': '.-..',
             'ł': '.-..-',   'm': '--',     'n': '-.',     'ń': '--.--',
             'ñ': '--.--',   'o': '---',    'ó': '---.',   'ò': '---.',
             'ö': '---.',    'ô': '---.',   'ø': '---.',   'p': '.--.',
             'q': '--.-',    'r': '.-.',    's': '...',    'ś': '...-...',
             'ş': '.--..',   'ș': '----',   'š': '----',   'ŝ': '...-.',
             'ß': '...--..', 't': '-',      'þ': '.--..',  'u': '..-',
             'ü': '..--',    'ù': '..--',   'ŭ': '..--',   'û': '..--',
             'v': '...-',    'w': '.--',    'x': '-..-',   'y': '-.--',
             'z': '--..',    'ž': '--..-',  'ź': '--..-',  'ż': '--..-.',
             '1': '.----',   '2': '..---',  '3': '...--',  '4': '....-',
             '5': '.....',   '6': '-....',  '7': '--...',  '8': '---..',
             '9': '----.',   '0': '-----',  ',': '--..--', '.': '.-.-.-',
             ';': '-.-.-',   ':': '---...', '/': '-..-.',  '-': '-....-',
             "'": '.----.',  '"': '.-..-.', '?': '..--..', '¿': '..-.-',
             '!': '-.-.--',  '¡': '--...-', '@': '.--.-.', '$': '...-..-',
             '&': '.-...',   '(': '-.--.',  ')': '-.--.-', '_': '..--.-',
             '=': '-...-',   '+': '.-.-.'}
    # Message
    message = [x for x in message.lower() if x == ' ' or x in morse.keys()]
    message = message[0] + ''.join(x for xInd, x in enumerate(message[1:], 1)
                                   if message[xInd] != ' '
                                   or message[xInd - 1] != ' ')
    message = message.strip(' ').split(' ')

    ## Encipher
    for x in message:
        if x == 'error':
            cipher.append('........'); continue
        word = []
        for y in x:
            if çTR and y == 'ç': word.append('.-.-')
            elif ðHR and y == 'ð': word.append('..-..')
            elif èIT and y == 'è': word.append('..-..')
            else:
                try: word.append(morse[y])
                except: pass
        if word != []: cipher.append(letSep.join(word))
    cipher = wordSep.join(cipher)

    ## Return cipher
    return cipher

# Decipher
def decipher_morse(cipher, letSep=' ', wordSep=' / ', ucase=False,
                   lang='gl;es;pt;de;fr;tr;it;pl;ro;hr;hu;da;eo;is'):

    '''
    decipher_morse(cipher, letSep=' ', wordSep=' / ', ucase=False,
                   lang='gl;es;pt;de;fr;tr;it;pl;ro;hr;hu;da;eo;is')

    Translates morse code to letters.

    Arguments:
    cipher -- Morse code being deciphered
    letSep -- String that separates letters in cipher
    wordSep -- String that separates words in cipher
    ucase -- False to return all lowercase letters, True for all uppercase
    lang -- String of ISO 639-1 language codes sepqrated by ';' used for
            characters with diacritics, gl stands for widely used global
            characters

    Steps:
    1. The cipher is separated based on wordSep, then letSep for each letter.
    2. The lang argument is simplified into 13 ISO 639-1 language codes, and
       one 'gl'
       Spanish   │ es
       Portugese │ pt
       German    │ de
       French    │ fr
       Turkish   │ tr
       Italian   │ it
       Polish    │ pl
       Romanian  │ ro
       Croatian  │ hr
       Hungarian │ hu
       Danish    │ da  Note: Also applies to Norwegian and Faroese
       Esperanto │ eo
       Icelandic │ is
    3. Each morse sequence is translated based on morse dictionaries. If one
       dictionary doesn't have the sequence, the next dictionary in lang is
       searched through. Morse dictionaries:
       .- a     -... b    -.-. c    -.. d    . e      ..-. f   --. g
       .... h   .. i      -..-- ï   .--- j   -.- k    .-.. l   -- m
       -. n     --- o     .--. p    --.- q   .-. r    ... s    ...-... ś
       ...-. ŝ  ...--.. ß - t       ..- u    ...- v   .-- w    -..- x
       -.-- y   --.. z    --..-. ż  .---- 1  ..--- 2  ...-- 3  ....- 4
       ..... 5  -.... 6   --... 7   ---.. 8  ----. 9  ----- 0  --..-- ,
       .-.-.- . ---... :  -....- -  .----. ' .-..-. " ..--.. ? -.-.-- !
       --...- ¡ .--.-. @  ...-..- $ .-... &  -.--.- ) ..--.- _ -...- =
       .-.-. +  ........ error
       gl: .--.- à  .-.- ä   ..-.. ë  ---. ò   ---- š  ..-- ü   -..-. /
           -.-.- ;  -.--. (
       es: .--.- á  ---- ch  ..-.. é  --.-- ñ  ..-.- ¿
       pt: ..-.- ão -.-.. ç  ---- ch  ---. ões
       de: ---- ch
       fr: -.-.. ç  ---- ch  ..-.. é  .-..- è  -..-. ê ..-- û
       tr: .-.- ç   --.-. ğ  .-..- i
       it: ..-.. è  .---. ì  ---. ò   ..-- ù
       pl: .-.- ą   -.-.. ć  ---. cz  ..-.. ę  --.-- ń -.-.- sz --..- ź
       ro: .--.- â  ---- ș
       hr: -.--. č  --.-. dž .---. lj --.-- nj --..- ž
       hu: .--.- á  --.-- ny
       da: .--.- å  .-.- æ   ---. ø
       eo: -.-.. ĉ  --.-. ĝ  ---- ĥ   .---. ĵ  ..-- ŭ
       is: .--.- á  .--.. þ
    4. Each word is put together and the word list is joined with spaces.

    Returns the message and revised lang string.
    '''

    ## Variables
    # General
    message = []
    # Cipher
    cipher = ''.join(x for x in cipher if x in '.-' + letSep + wordSep)
    for x in ''.join(x for x in set(letSep + wordSep) if x not in '.-'):
        cipher = cipher.strip(x)
    cipher = cipher.split(wordSep)
    # Lang
    if lang is None: lang = 'gl;es;pt;de;fr;tr;it;pl;ro;hr;hu;da;eo;is'
    lang = lang.lower().strip(';').split(';')
    langs = ['gl', 'es', 'pt', 'de', 'fr', 'tr', 'it',
             'pl', 'ro', 'hr', 'hu', 'da', 'eo', 'is']
    lang = [x for x in lang if x in langs] \
           + [x for x in langs if x not in lang]
    lang = ['morse'] + [x.upper() for x in lang]
    # Dictionaries
    morse = {'.-': 'a',      '-...': 'b',   '-.-.': 'c',    '-..': 'd',
             '.': 'e',       '..-.': 'f',   '--.': 'g',     '....': 'h',
             '..': 'i',      '-..--': 'ï',  '.---': 'j',    '-.-': 'k',
             '.-..': 'l',    '--': 'm',     '-.': 'n',      '---': 'o',
             '.--.': 'p',    '--.-': 'q',   '.-.': 'r',     '...': 's',
             '...-...': 'ś', '...-.': 'ŝ',  '...--..': 'ß', '-': 't',
             '..-': 'u',     '...-': 'v',   '.--': 'w',     '-..-': 'x',
             '-.--': 'y',    '--..': 'z',   '--..-.': 'ż',  '.----': '1',
             '..---': '2',   '...--': '3',  '....-': '4',   '.....': '5',
             '-....': '6',   '--...': '7',  '---..': '8',   '----.': '9',
             '-----': '0',   '--..--': ',', '.-.-.-': '.',  '---...': ':',
             '-....-': '-',  '.----.': "'", '.-..-.': '"',  '..--..': '?',
             '-.-.--': '!',  '--...-': '¡', '.--.-.': '@',  '...-..-': '$',
             '.-...': '&',   '-.--.-': ')', '..--.-': '_',  '-...-': '=',
             '.-.-.': '+',   '........': 'error'}
    GL = {'.--.-': 'à', '.-.-': 'ä', '..-..': 'ë', '---.': 'ò', '----': 'š',
          '..--': 'ü', '-..-.': '/', '-.-.-': ';', '-.--.': '('}
    ES = {'.--.-': 'á', '----': 'ch', '..-..': 'é', '--.--': 'ñ',
          '..-.-': '¿'}
    PT = {'..-.-': 'ão', '-.-..': 'ç', '----': 'ch', '---.': 'ões'}
    DE = {'----': 'ch'}
    FR = {'-.-..': 'ç', '----': 'ch', '..-..': 'é', '.-..-': 'è',
          '-..-.': 'ê', '..--': 'û'}
    TR = {'.-.-': 'ç', '--.-.': 'ğ', '.-..-': 'i'}
    IT = {'..-..': 'è', '.---.': 'ì', '---.': 'ò', '..--': 'ù'}
    PL = {'.-.-': 'ą', '-.-..': 'ć', '---.': 'cz', '..-..': 'ę', '--.--': 'ń',
          '-.-.-': 'sz', '--..-': 'ź'}
    RO = {'.--.-': 'â','----': 'ș'}
    HR = {'-.--.': 'č', '--.-.': 'dž', '.---.': 'lj', '--.--': 'nj',
          '--..-': 'ž'}
    HU = {'.--.-': 'á', '--.--': 'ny'}
    DA = {'.--.-': 'å', '.-.-': 'æ', '---.': 'ø'}
    EO = {'-.-..': 'ĉ', '--.-.': 'ĝ', '----': 'ĥ', '.---.': 'ĵ', '..--': 'ŭ'}
    IS = {'.--.-': 'á', '.--..': 'þ'}

    ## Decipher
    for x in cipher:
        word = ''
        x = x.split(letSep)
        for y in x:
            for z in lang:
                try: letter = eval(z + "['" + y + "']"); break
                except KeyError: pass
            try: word += letter
            except NameError: continue
        message.append(word)
    message = ' '.join(message)
    if ucase: message = message.upper()
    lang = ';'.join(lang[1:]).lower()

    ## Return message and lang
    return message, lang
