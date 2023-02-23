# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.morse_funcs import encipher_morse, decipher_morse

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input separators
    askSep = inpYN('Choose word/letter separators? ')
    if askSep:
        letSep = inpText('Morse letter separator: ', 'text')
        wordSep = inpText('Morse word separator: ', 'text')
    else:
        print('Letter separators are " ". Word separators are " / ".')
        letSep = ' '
        wordSep = ' / '

    # Input message/cipher
    m_c = inpText(None, (('.-', letSep, wordSep), None)[e_d], e_d, lCase=True)

    # Encipher
    if e_d:
        if 'ç' in m_c:
            çTR = inpYN('Should the ç character be translated in its Turkish'
                        + ' format?')
        else:
            çTR = False
        if 'ð' in m_c:
            ðHR = inpYN('Should the ð character be translated in its Croatian'
                        + ' format?')
        else:
            ðHR = False
        if 'è' in m_c:
            èIT = inpYN('Should the è character be translated in its Italian'
                        + ' format?')
        else:
            èIT = False
        cipher = encipher_morse(m_c, letSep, wordSep, çTR, ðHR, èIT)
        print('\n' + cipher + '\n')

    # Decipher
    else:
        ucase = inpChoice('Should the message be all lowercase (0) or all '
                          + 'uppercase (1)? ')
        if inpYN('Are there any specific languages that should be prioritized'
                 + ' before other languages for special characters like à and'
                 + ' è? '):
            print('''
ISO 639-1 Language codes from most spoken to least spoken:

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

An added code: gl (global), for any international double-meaning morse
sequences, recommended to go first.

Write the codes from most important to least important.
Non-codes will be discarded.
If some codes aren't listed, they will be automatically added.
''')
            lang = inpList(False, 'language codes', None,
                           True, True, False, True)
            lang = ';'.join(lang)
        else:
            lang = None
        a, b = decipher_morse(m_c, letSep, wordSep, ucase, lang)
        print('\nMessage: ' + a + '\nLanguage sequence: '
              + ', '.join(b.split(';')).upper())
