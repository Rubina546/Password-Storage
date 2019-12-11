# Password Storage
final project for a class about Python. 
It's an application that opens up with an admin password, and you have to know this beforehand. 
Its hard coded within the code itself. This unlocks access to keywords to obtain passwords related
to those key words. For example; using the key word chase will return the password from the users 
chase account. If its the users first time using that key word it will prompt the user to enter a
password related to that key word. All of this is safe because I used an encyrption method known as 
vernam cypher. I had encorporated Vigenere and Caesar cypher as well. From a security stand point, 
vernam cypher made the most sense, since it utilizes a random keystream and encrypts the plaintext 
to something that has no relation to the encrypted text, therefore, a hacker would have a hard time
decrypting the encrypted text. This is much more secure when compared to Caesar cypher since an 
outside viewer could guess the key based on shifting each inidividual character until something is
correctly decrypted.   
