# Import
import sys
from ntpath import dirname as d
sys.path.insert(0, d(d(__file__)))
try: from _variables_ import *
except ModuleNotFoundError: from ._variables_ import *
from cipher_funcs.xor_funcs import encipher_xor, decipher_xor

# UI
def ui():

    # Input encipher/decipher
    e_d = inpED()

    # Input message/cipher
    m_c, m_cBin = inpList(('cipher', 'message')[e_d], True, False, maxNum=255)

    # Input key
    key, keyBin = inpList('key', True, False, maxNum=255)

    # Print ciphers/messages
    if e_d:
        a, b, c = encipher_xor(m_c, key, m_cBin, keyBin)
        print('\nBinary cipher: ' + a + '\nDecimal cipher: ' + str(b)
              + '\nString cipher: ' + c + '\n')
    else:
        a, b, c = decipher_xor(m_c, key, m_cBin, keyBin)
        print('\nBinary message: ' + a + '\nDecimal message: ' + str(b)
              + '\nString message: ' + c + '\n')
