import sys
sys.path.append('../my_module')

from PasswordStorage import PasswordStorage

# Script to run the password prompt.
print("Enter the password to the system: ")
usr_password = sys.stdin.readline().rstrip()

paa = PasswordStorage( usr_password)
paa.update_file()
print("Press 'c' to continue or anything else to quit")

# keep asking the user if they want to keep checking for passwords using keywords.
while sys.stdin.readline().rstrip() == 'c':
    paa.decoded_password = None
    paa.decoded_password = paa.decode_password(paa.get_key())
    if paa.decoded_password != None:
        print("Your password is: " + paa.get_password())

    print("Press 'c' to continue or anything else to quit")

    paa.update_file()