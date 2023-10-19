# Problem 3 - Caesar Cipher and Decrypt
# Author: Carter Harms
 

# imports
import string
import sys


# Create values for ASCII upper and lowercase string characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase


def caesar_encrypt(key, message):

    #Create empty encryption string
    encryption = ""

    # Validate key is an interger
    try:
        key = int(key)
    except ValueError:
        print("Key was not an integer")
        sys.exit()

    # Create loop for each character value in a string
    for i in range(len(message)):
        val = message[i]

        # Return different values depending on the initial value of the character in the string
        if val.isspace():
            encryption += " "
        elif val.isdigit():
            encryption += val
        elif (val.isupper()):
            encryption += chr((ord(val) + key - 65) % 26 + 65)
        elif (val.islower()):
            encryption += chr((ord(val) + key - 97) % 26 + 97)
        elif val in "!@#$%^&*":
            encryption += val
    
    return encryption
    




def caesar_decrypt(key, message):

    # Create empty decryption string
    decryption = ""

    # Validate key is an interger
    try:
        key = int(key)
    except ValueError:
        print("Key was not an integer")
        sys.exit()

    # Create loop for each character value in a string
    for i in range(len(message)):
        val = message[i]

        # Return different values depending on the initial value of the character in the string
        if val.isspace():
            decryption += " "
        elif val.isdigit():
            decryption += val
        elif (val.isupper()):
            decryption += chr((ord(val) - key))
        elif (val.islower()):
            decryption += chr((ord(val) - key))
        elif val in "!@#$%^&*":
            decryption += val
    
    return decryption

# upper F (70) -> upper A (65)
    

# Footnote references
# ref: https://gist.github.com/AO8/3a89ba7c8f032c7a1ff505baa3ce970e
# ref: https://www.scaler.com/topics/caesar-cipher-python/
# ref: https://stackoverflow.com/questions/16060899/alphabet-range-in-python
# ref: https://stackoverflow.com/questions/495228/unicode-of-lower-case-and-upper-case-letters
# ref: https://www.geeksforgeeks.org/ascii-table/
