# Problem 5 - Crack a Cipher
# Author: Carter Harms

# ref: https://stackoverflow.com/questions/1909619/python-list-to-integers

import string

# Message to decrypt
message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

def caesar_decrypt_nokey(message):

    message = list(message)

    # Create empty list to gather the 26 decryption option messages
    decrypted_messages = []
    
    # Create a loop of 26, designed to loop through the alphabet for decrypting the key
    for dig in range(26):

        decryption = ''
        
        # Assigning potential values to each of the encrypted characters in the message 
        for i in range(len(message)):
            val = message[i]
            if val.isspace():
                decryption += " "
            elif val.isdigit():
                decryption += val
            elif (val.islower()):
                decryption += chr((ord(val) - dig) % 26 + 97)
            elif val in "!@#$%^&*":
                decryption += val

        # Appending to the list, 26 options for potential decrypted messages
        decrypted_messages.append(decryption)
        print(decrypted_messages)

    # Opening the 1000 most common words text file
    filename = 'common_words.txt'

    words = []
    try:
        f_contents = open(filename, 'r')
    # Create error message if incorrect filename
    except OSError:
        print("Not a proper filename")

    
    # Read through file
    with open (filename) as fin:
        for line in fin:
            # Create list of words and strip whitespace characters
            words.append(line.strip())


    # Create a alphabetically sorted list of all the words in the text file

    # Close the text file
    f_contents.close()


    for s in decrypted_messages:
        for item in words:
            if item in s:
                print(s)
            