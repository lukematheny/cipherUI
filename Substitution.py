# Import
from cipher_ui.substitution_ui import ui

# Variables
cNo = ['0', 'n', 'no', 'zero', 'false']
cYes = ['1', 'ok', 'okay', 'one', 'y', 'yeah', 'yes', 'true']

# Main
def main():
    
    # Loop
    while True:

        # UI
        ui()
        
        # Input loop
        while True:
            loop = input('Again? ').lower()
            if loop in cNo + cYes: break
            else: print('\nNot recognized, try again.\n')
        if loop in cNo: break
        else: print()

# Name is main
if __name__ == '__main__':
    main()