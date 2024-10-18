'''7. Password Generator
Concepts: String manipulation, Random module
Description: Generate a strong password based on user 
specifications (e.g., length, inclusion of special characters, numbers, etc.).'''

import random 
import string
length =int(input("Enter the length of password:"))

print('''\n Choose character set to get the password from these :
       1. Digits
       2. Letters
       3. Special Characters 
       4. Exit''')

characterlist = ""
while(True):
    choice = int(input("Pick a number:"))
    if (choice == 1):
        characterlist += string.ascii_letters
    elif (choice == 2):
        characterlist += string.digits
    elif (choice == 3):
        characterlist += string.punctuation
    elif (choice == 4):
        break
else:
    print("Please pick a valid option!")

password = []
for i in range(length):

    randomchar = random.choice(characterlist)
    password.append(randomchar)

print("The random password is"+"".join(password))

