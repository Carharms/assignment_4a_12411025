# Problem - Farenheit to Celsuis
# Author: Carter Harms


while True:
    try:
        # Ask for user input in Fahrenheit
        fahrenheit_temp = int(input("Enter a temperature in Fahrenheit: "))
        # Set parameter that Farenheit must be a positive number
        if fahrenheit_temp < 0:
            print("Please enter a positive, whole number numeric temperature.")
            continue
        elif fahrenheit_temp >=0:
            break
    # Set parameter that farenheit_temp must be an interger
    except ValueError:
        print("Please enter a positive, whole number numeric temperature.")


# Fahrenheit to Celsius Formula: ((F-32)*5)/9
celsius_temp = ((fahrenheit_temp - 32) * 5) / 9
# round celsius_temp to 2 decimal places
celsius_temp = round(celsius_temp, 2)

# output temperature in Celsius
print(f"The temperature is {celsius_temp} in Celsius.")


# Footnote References
# ref: https://stackoverflow.com/questions/63437196/how-to-re-ask-for-user-input-if-user-inputted-a-non-integer-in-python