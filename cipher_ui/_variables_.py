# Import
from string import ascii_lowercase as low, ascii_uppercase as up, \
                   ascii_letters as let, digits

# Misc
letNum = let + digits
__all__ = ['low', 'up', 'let', 'letNum', 'digits', 'cNo', 'cYes', 'cRandom',
           'notRec', 'mustHtext', 'mustHlet', 'mustHnum', 'mustHletNum',
           'mustBint', 'mustBlet', 'mustBnum', 'mustBletNum', 'mustB1chr',
           'eLet', 'eNum', 'eLetNum', 'dLet', 'dNum', 'dLetNum', 'inpED',
           'inpMethod', 'inpYN', 'inpList', 'inpChoice', 'inpPlayfair',
           'inpChr', 'inpText', 'inpNum']

## Warnings
# Not...
notRec = '\nNot recognized, try again.\n'
# Must have...
mustHtext = '\nMust have text, try again.\n'
mustHlet = '\nMust have letter(s), try again.\n'
mustHnum = '\nMust have number(s), try again.\n'
mustHletNum = '\nMust have letter(s)/number(s), try again.\n'
# Must be...
mustBint = '\nMust be an integer, try again.\n'
mustBlet = '\nMust be a letter, try again.\n'
mustBnum = '\nMust be a number, try again.\n'
mustBletNum = '\nMust be a letter or number, try again.\n'
mustB1chr = '\nMust be one character, try again.\n'
# ...won't be enciphered
eLet = "Non-letters won't be enciphered."
eNum = "Non-numbers won't be enciphered."
eLetNum = "Non-letters/non-numbers won't be enciphered."
# ...won't be deciphered
dLet = "Non-letters won't be deciphered."
dNum = "Non-numbers won't be deciphered."
dLetNum = "Non-letters/non-numbers won't be deciphered."

## Lists
cNo = ['0', 'n', 'no', 'zero', 'false']
cYes = ['1', 'ok', 'okay', 'one', 'y', 'yeah', 'yes', 'true']
cRandom = ['rand', 'random']
stringH = ['low', 'up', 'let', 'digits', 'letNum', 'text']
stringB = ['low', 'up', 'let', 'digits', 'letNum', 'integer', 'number']
strDictH = {'low': 'lowercase letter(s)', 'up': 'uppercase letter(s)', 'let':
            'letter(s)', 'digits': 'number(s)', 'letNum': 'letter(s)/'
            + 'number(s)'}
strDictB = {'low': 'non-lowercase letters', 'up': 'non-uppercase letters',
            'let': 'non-letters', 'digits': 'non-numbers', 'numbers':
            'non-numbers', 'letNum': 'non-letters/non-numbers', 'integers':
            'non-integers'}

## Functions
# Encipher/Decipher input
def inpED(inputText='Encipher (0) or decipher (1)? '):
    '''Input encipher/decipher choice.'''
    return inpChoice(inputText, [True, False])

# Method input
def inpMethod():
    '''Input method choice.'''
    return inpChoice('Method 1 or 2? ', {'1': True, 'one': True,
                                         '2': False, 'two': False}, False)

# Yes/No input
def inpYN(inputText, inv=False):
    '''Input a choice between yes and no.'''
    while True:
        i = input(inputText).lower()
        if i in cYes + cNo: break
        print(notRec)
    return (i in cYes, i in cNo)[bool(inv)]

# Choice input
def inpChoice(inputText, dictList=[False, True], num=True, exc=None):
    '''Input a choice between objects in a list/dictionary.'''
    while True:
        i = input(inputText).lower()
        if bool(num):
            try: i = float(i)
            except ValueError: print(notRec); continue
            if i == int(i): i = int(i)
            else: print(mustBint); continue
        try: dictList[i]; break
        except (IndexError, KeyError):
            print((exc, notRec)[exc == None]); continue
    return dictList[i]

# Number input
def inpNum(inputText, flt=False, minNum=None, maxNum=None, minLen=None,
           maxLen=None):
    '''Input a number.'''
    while True:
        try: i = float(input(inputText))
        except ValueError: print(mustBnum); continue
        if not flt and i == int(i): i = int(i)
        elif not flt: print(mustBint); continue
        if minNum != None and i < minNum:
            print('\nMust be at least ' + str(minNum) + ', try again.\n')
            continue
        if maxNum != None and i > maxNum:
            print('\nMust be at most ' + str(maxNum) + ', try again.\n')
            continue
        if minLen != None and len(str(i)) < minLen:
            print('\nMust be at least ' + str(minLen)
                  + ' digits long, try again.\n')
            continue
        if maxLen != None and len(str(i)) > maxLen:
            print('\nMust be at most ' + str(maxLen)
                  + ' digits long, try again.\n')
            continue
        break
    return i

# Playfair input
def inpPlayfair(askMixed=False, defaultSqLn=5, ask5v6=False, text5v6=None,
                twice=[False, 'For first key:', 'For second key:'],
                textKey=None, textMix=None):
    '''Input a Playfair key.'''
    if not isinstance(defaultSqLn, int): raise TypeError
    if not defaultSqLn in [5, 6]: raise ValueError
    if len(twice) != 3: raise ValueError
    if bool(ask5v6):
        while True:
            s = ('', 's')[bool(twice[0])]
            nums = input((text5v6, '5x5 Playfair key' + s + ' (0) or 6x6 '
                          + 'Playfair key' + s + ' (1)? ')[text5v6 == None])
            try: nums = float(nums)
            except ValueError: print(notRec); continue
            if nums in [0, 1]: nums = bool(nums); break
            print(notRec)
    else: nums = defaultSqLn == 6
    t, key, twice[0] = 0, [], bool(twice[0])
    while True:
        if twice[0]: print(twice[(1, 2)[t == 1]])
        if bool(askMixed):
            while True:
                mix = input((textMix, 'Mixed alphabet (0) '
                             + 'or Playfair key (1)? ')[textMix == None])
                try: mix = float(mix)
                except ValueError: print(notRec); continue
                if mix in [0, 1]: mix = not bool(mix); break
                print(notRec)
        else: mix = False
        if mix: key1 = None
        else: key1 = input((textKey, 'Playfair key: ')[textKey == None])
        if twice[0] and t == 0: key.append(key1)
        elif twice[0] and t == 1: key = tuple(key + [key1]); break
        else: key = key1; break
        t += 1
    return key, nums

# Single character input
def inpChr(inputText, mustB=None, rand=False, exc=None, lCase=False):
    '''Input a single character or random.'''
    # Variables
    rand, lCase = bool(rand), bool(lCase)
    # Change
    if mustB != None:
        # Clean up wrong types
        if not isinstance(mustB, (str, tuple, list)): raise TypeError
        if isinstance(mustB, (tuple, list)):
            for x in mustB:
                if not isinstance(x, str): raise TypeError
        else: mustB = [mustB]
        # Simplify & document
        mustB = [x.lower() for x in mustB if x.lower() != 'text']
        inc, n = '', 0
        for x in mustB:
            if x in stringB:
                if x in stringH: inc += eval(x)
                elif x == 'integer': n = 1
                else: n = 2
            else: inc += x
    elif rand: raise ValueError
    # Input
    while True:
        i = input(inputText)
        if lCase: i = i.lower()
        if mustB != None:
            if rand and i in cRandom: i = 'random'; break
            if len(i) != 1: print(mustB1chr); continue
            elif n > 0:
                try: i = float(i)
                except ValueError: print(mustBnum); continue
                if i == int(i): i = int(i)
                elif n == 1: print(mustBint); continue
                break
            elif len(i) == 1 and i in inc: break
            print((exc, notRec)[exc == None])
        else:
            if len(i) != 1: print(mustB1chr); continue
            break
    # Return
    return i

# List input
def inpList(askFor='message', askBin=False, strOnlyAB=True, minNum=None,
            maxNum=None, minLen=None, maxLen=None):
    # Input type, True for digits, False for characters
    inpType = inpChoice('Is the ' + askFor + ' comprised of characters (0) '
                        + 'or digits (1)? ')
    # Input characters
    if not inpType:
        i = inpText(askFor.capitalize() + ': ', (None, 'let')[strOnlyAB], True,
                    True, True, False, [False, 'let', True], None, minLen,
                    maxLen)
        if strOnlyAB:
            i = ''.join(x for x in i if x in let)
        binary = False
    # Input digits
    else:
        # Ask if list of numbers or one number with its digits as the list
        listInput = inpChoice('Is the ' + askFor + ' a list of numbers (0) or '
                              + 'one number with its digits as the list (1)? ',
                              [True, False])
        # Binary numbers
        if askBin: binary = inpYN('Are the numbers going to be in binary? ')
        else: binary = False
        # List
        if listInput:
            # Input list
            while True:
                print('Write the ' + askFor + ' with a space between each '
                      + 'number.')
                i = inpText(askFor.capitalize() + ': ').strip(' ')
                i = i[0] + ''.join(x for xInd, x in enumerate(i[1:], 1) \
                                   if i[xInd] != ' ' or i[xInd - 1] != ' ')
                # Check if numbers are numbers
                if any(x not in digits + ' ' for x in i):
                    print('\nUnrecognized characters, try again.\n')
                    continue
                # Check if numbers are binary
                if binary:
                    if any(x not in '01 ' for x in i):
                        print('\nNumbers must be binary, try again.\n')
                        continue
                # Check if minNum >= x >= maxNum
                i = i.split(' ')
                if binary:  # Binary
                    if any(len(x.lstrip('0')) > 8 for x in i):
                        print('\n')
                else:  # Decimal
                    for x in i:
                        if isinstance(minNum, int) and int(x) < minNum:
                            print('\nNo number can be less than ' + str(minNum)
                                  + ', try again.\n')
                            restart = True; break
                        else: restart = False
                        if isinstance(maxNum, int) and int(x) > maxNum:
                            print('\nNo number can be more than ' + str(maxNum)
                                  + ', try again.\n')
                            restart = True; break
                        else: restart = False
                if restart: continue
                i = [int(x) for x in i]
                break
        # Input number
        else:
            while True:
                if binary:
                    print('Each 8 numbers will be read as one binary digit.')
                i = inpText(askFor.capitalize() + ': ', 'digits')
                i = ''.join(x for x in i if x in digits)
                # Check if numbers are binary
                if binary and any(x not in '01' for x in i):
                    print('\nNumbers must be binary, try again.\n'); continue
                i = int(i)
                break
    return i, binary

# Text input
def inpText(inputText=None, mustH=None, ed=True, m=True, w=True, lCase=False,
            knl=[False, 'let', True], knlText=None, minLen=None, maxLen=None):
    '''Input a line of text.'''
    # Variables
    inc, ed, m, w = '', bool(ed), bool(m), bool(w)
    if inputText == None: inputText = ('Cipher: ', 'Message: ')[ed]
    # Change
    if mustH != None:
        # Clean up wrong types
        if not isinstance(mustH, (str, tuple, list)): raise TypeError
        if isinstance(mustH, (tuple, list)):
            for x in mustH:
                if not isinstance(x, str): raise TypeError
        else: mustH = [mustH]
        if isinstance(knl, tuple): knl = list(knl)
        if len(knl) != 3: raise ValueError
        # Simplify
        mustH = [x.lower() for x in mustH if x]
        for xInd, x in enumerate(mustH):
            if x == 'letnum': mustH[xInd] = 'letNum'
        if 'low' in mustH and 'up' in mustH: mustH.append('let')
        if 'let' in mustH:
            mustH = [x for x in mustH if x not in ('low', 'up')]
        if 'let' in mustH and 'digits' in mustH:
            mustH = [x for x in mustH if x not in ('let', 'digits')]
            mustH.append('letNum')
        t = 'text' in mustH
        mustH = [x for x in mustH if x not in stringH] \
                + [x for x in mustH if x in stringH and x != 'text']
        # Document non-default characters
        for x in mustH:
            if x in stringH:
                for y in eval(x): inc = inc.replace(y, '')
            else: inc += x
        inc = ''.join(sorted(set(inc), key=inc.index))
        mustH = [x for x in mustH if x in stringH]
        # Must and won't statements from past variables
        extras = inc != ''
        if extras: mustH.append(inc)
        if len(mustH) == 1 and mustH[0] in ['let', 'digits', 'letNum']:
            if m:
                if mustH[0] == 'digits': mustH[0] = 'num'
                must = eval('mustH' + mustH[0])
            if w:
                if mustH[0] in ['digits', 'num']: mustH[0] = 'num'
                wont = mustH[0][0].upper() + mustH[0][1:]
                wont = eval(('d' + wont, 'e' + wont)[ed])
        # New must and won't statements
        elif len(mustH) != 0:
            # Must
            if m:
                must = [strDictH[x] for x in (mustH, mustH[:-1])[extras]]
                if extras: must.append('characters in ' + mustH[-1])
                if len(mustH) == 1: must = must[0]
                elif len(mustH) == 2: must = ' or '.join(must)
                else: must = ', '.join(must[:-1]) + ', or ' + must[-1]
                must = '\nMust have ' + must + ', try again.\n'
            # Won't
            if w:
                wont = [strDictB[x] for x in (mustH, mustH[:-1])[extras]]
                if extras: wont.append('non-characters in ' + mustH[-1])
                if len(mustH) == 1: wont = wont[0]
                elif len(mustH) == 2: wont = ' and '.join(wont)
                else: wont = ', '.join(wont[:-1]) + ', and ' + wont[-1]
                wont = wont[0].upper() + wont[1:] + " won't be " \
                       + ('deciphered.', 'enciphered.')[ed]
        # Keep non-letters statement
        knl[0] = bool(knl[0])
        if knl[0]:
            # Clean up wrong types
            if not isinstance(knl[1], (str, tuple, list)): raise TypeError
            if isinstance(knl[1], (tuple, list)):
                for x in knl[1]:
                    if not isinstance(x, str): raise TypeError
            else: knl[1] = [knl[1]]
            knl[1] = [x for x in knl[1] if x not in stringB] \
                     + [x for x in knl[1] if x in stringB]
            # Include
            inc2 = ''
            for x in knl[1]:
                if x in stringB:
                    for y in eval(x): inc2.replace(y, '')
                else: inc2 += x
            knl[1] = [strDictB[x] for x in knl[1] if x in stringB] \
                     + ([], ['characters in ' + inc2])[inc2 != '']
            # Join
            if len(knl[1]) == 1: knl[1] = knl[1][0]
            elif len(knl[1]) == 2: knl[1] = ' or '.join(knl[1])
            else: knl[1] = ', '.join(knl[1][:-1]) + ', and ' + knl[1][-1]
        # Complete inc
        for xInd, x in enumerate(mustH):
            if x in ['num', 'Num']: x = 'digits'
            if x in stringH: inc += eval(x)
    # Fill in blanks
    else: t = False
    # Input
    while True:
        i = input(inputText)
        if bool(lCase): i = i.lower()
        if t and i == '': print(mustHtext); continue
        if isinstance(minLen, int) and len(i) < minLen:
            print('\nMust be at least ' + str(minLen)
                  + ' characters long, try again.\n')
            continue
        if isinstance(maxLen, int) and len(i) > maxLen:
            print('\nMust be at least ' + str(maxLen)
                  + ' characters long, try again.\n')
            continue
        if inc != '':
            if m and all(x not in inc for x in i): print(must); continue
            if w and any(x not in inc for x in i):
                if bool(knl[0]):
                    knl = inpYN((knlText, 'Keep ' + knl[1]
                                 + ' in encryption? ')[knlText == None])
                    i = (i, knl)
                else: print(wont)
            elif bool(knl[0]): i = (i, bool(knl[2]))
        break
    # Return
    return i
