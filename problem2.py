# Problem 2 - Is Number
# Author: Carter Harms


astring = input("Enter a number: ")

def isnumber(astring):
    # Convert string to interger
    try:
        astring = int(astring)
        success = True
    # Create error if string cannot be converted to interger
    except ValueError:
        success = False

    # Deliver True value if string is a number
    if success == True:
        print(True)
    # Deliver False value if string is not a number
    elif success == False:
        print(False)

isnumber(astring)