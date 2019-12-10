#It's an application that opens up with an admin password, and you have to know this beforehand. 
#Its hard coded within the code itself. This unlocks access to keywords to obtain passwords related to those 
#key words. For example; using the key word chase will return the password from the users chase account. If its the 
#users first time using that key word it will prompt the user to enter a password related to that key word. All of 
#this is safe because I used an encyrption method known as vernam cypher.



import sys

class PasswordStorage:
    """
        Implements Password storage using file.txt and encrypts password.

    """

    # global variables
    password = "hello world"
    decoded_password = ""
    file = "files.txt"
    # used for caesar key:
    # caesar_key = 0
    attempt = 0
    password_table = {}


    def __init__(self, password):
        """ Initialize the object by validating password, the decrypt.

        """
        self.setup_password_table()
        self.validate_password(password)
        key = self.get_key()
        self.decoded_password = self.decode_password(key)
        if self.decoded_password != None:
            print("Your password is: " + self.decoded_password)

    def get_password(self):
        """ return password to display to user."""
        return self.decoded_password
    def get_key(self):
        """ Ask the user to input the keyword

        """
        print("Please enter keyword to get your password: ")
        return sys.stdin.readline().rstrip()
    def setup_password_table(self):
        """ setup the dictionary properly.

        """
        fp = open(self.file)
        line = fp.readline()
        while(line):
            print(line)
            if line == '\n': break;
            (key, val) = line.split(',')
            self.password_table[str(key)] = val
            line = fp.readline()
        fp.close()
    def update_file(self):
        """ update the file.txt document to store the keyword and encrypted password

        """
        fp = open(self.file, "w")
        for key, val in self.password_table.items():
            fp.write(key + "," + val + "\n")
        fp.close()

    def decrypt(self, cyphertext):
        """ decrypt the cypher text

        """
        # Caesar Cypher
        # return self.caesar_shift((-1*caesar_key), cyphertext)

        # Vigenere Cypher
        #return self.original_text(cyphertext, key)
        # Vernam Cypher
        return self.make_vernam_cypher(cyphertext, self.password)
    
    def decode_password(self, key_entered):
        """ check if the keyword has a password tied to it.

        """
        val = self.password_table.get(key_entered)
        if val == None:
            print("Could not locate key! Would you like to enter a password for the key [y|n]?")
            inp = sys.stdin.readline()
            inp = inp.rstrip()
            if inp == "y":
                self.prompt_insert_password(key_entered)
            return None
        else:
            return self.decrypt(val)


    def generate_key(self, string, key):
        """  This function generates the key in a cyclic manner
             Site used: https://www.geeksforgeeks.org/vigenere-cipher/
        """
        key = list(key)
        if len(string) == len(key):
            return (key)
        else:
            for i in range(len(string) -
                           len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

        # This function returns the

    # encrypted text generated
    # with the help of the key
    def cipher_text(self, string, key):
        """ This function returns the encrypted text generated with the help of the key
            Site used: https://www.geeksforgeeks.org/vigenere-cipher/
        """
        cipher_text = []
        for i in range(len(string)):
            x = (ord(string[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return ("".join(cipher_text))




    def original_text(self, cipher_text, key):
        """  This function decrypts the encrypted text and returns the original text
            Site used: https://www.geeksforgeeks.org/vigenere-cipher/
        """
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) -
                 ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return ("".join(orig_text))


    def make_vernam_cypher(self, text, key):
        """ Returns the Vernam Cypher for given string and key
            Site used: https://superdecade.blogspot.com/2015/10/vernam-cypther-in-python.html
        """
        answer = ""  # the Cypher text
        p = 0  # pointer for the key
        for char in text:
            answer += chr(ord(char) ^ ord(key[p]))
            p += 1
            if p == len(key):
                p = 0
        return answer

    def prompt_insert_password(self, key):
        """ Ask the user to insert a password, and then encrpy that password.

        """
        print("Please insert your password for the following keyword " + key + ": ")
        self.insert_password(key, sys.stdin.readline())
        
    def insert_password(self, key, password):
        # encrpyt the password
        self.password_table[key] = self.encrypt(password)

    def encrypt(self, password):
        """ Encrpyt password using Vernam Cypher

        """

        # Caesar Cypher
        # return self.caesar_shift(caesar_key, password)

        # Vigenere Cypher
        # key = self.generate_key(password, self.password)
        # return self.cipher_text(password, key)

        # Vernam Cypher
        return self.make_vernam_cypher(password, self.password)
    def caesar_shift(self, shift, password):
        """ Shift text by a certain number

        """

        new_string = ""
        for i in password:
            new_string += (chr((ord(i) + shift) % 255))
        return new_string
    def validate_password(self, password):
        """ Check if password entered by the user is correct.

        """

        password = password.rstrip()
        if self.password == password:
            print("Successfully Logged In!")
        else:
            print("Password was incorrect! - " + password)
            if self.attempt > 2:
                print("Ran out of attempts! Application will CLOSE NOW!")
                sys.exit()
            else:
                print(" Please re-enter your password: ")
                self.attempt += 1
                self.validate_password( sys.stdin.readline() )




