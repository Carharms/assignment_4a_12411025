# Problem 7 - Centered Average
# Author: Carter Harms

import sys


def centered_average_with_iteration(numbers):

    # ref: https://tutorial.eyehunts.com/python/how-to-sort-a-list-in-python-without-sort-function-example-code/

    # If/Else statement to confirm array has >=3 inputs
    if len(numbers) <= 2:
        print("Array has too few values")
        sys.exit()
    else:
        pass

    # Using iteration to sort elements of array

    # Creating a nested loop to loop through list, comparing 2 elements at a time
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            
            # Establishing order of two list elements being compared
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    sorted_numbers = numbers

    # Removing minimum and maximum of sorted-numbers list
    sorted_numbers.remove(max(sorted_numbers))
    sorted_numbers.remove(min(sorted_numbers))

    # Removing any duplicate values for maximum/minimum values within the list
    if sorted_numbers[0] == sorted_numbers[1]:
        sorted_numbers.remove(min(sorted_numbers))
    elif sorted_numbers[-1] == sorted_numbers[-2]:
        sorted_numbers.remove(max(sorted_numbers))
    else: pass

    # Establishing variable for length
    length = len(sorted_numbers)

    # Calculating the average using the sum of sorted_numbers / length variable
    total_value = sum(sorted_numbers)
    average = total_value / length
    return print(average)


def centered_average(numbers):
    
    # If/Else statement to confirm array has >=3 inputs 
    if len(numbers) <= 2:
        print("Array has too few values")
        sys.exit()
    else:
        pass


    # Using python build-in functions to sort an array
    sorted_numbers = sorted(numbers)

    # Removing minimum and maximum of sorted-numbers list
    sorted_numbers.remove(max(sorted_numbers))
    sorted_numbers.remove(min(sorted_numbers))


    # Removing any duplicate values for maximum/minimum values within the list
    if sorted_numbers[0] == sorted_numbers[1]:
        sorted_numbers.remove(min(sorted_numbers))
    elif sorted_numbers[-1] == sorted_numbers[-2]:
        sorted_numbers.remove(max(sorted_numbers))
    else: pass

    # Establishing variable for length
    length = len(sorted_numbers)

    # ref: https://stackoverflow.com/questions/11344827/summing-elements-in-a-list
    total_value = sum(sorted_numbers)
    average = total_value / length
    return print(average)
