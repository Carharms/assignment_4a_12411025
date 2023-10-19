# Problem 4 - Process a Text File
# Author: Carter Harms

filename = 'common_words.txt'

def process_file(filename):
    # Open and read the file
    words = list()
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

    # Use length function to determine number of lines in the text file
    number_of_lines = len(words) 

    # Create a alphabetically sorted list of all the words in the text file
    sorted_items = words.sort()

    # Close the text file
    f_contents.close()
    
    # Return relevant insights from the file
    return filename, sorted_items, number_of_lines
 

process_file(filename)


# Footnote references
# ref: https://www.geeksforgeeks.org/python-ways-to-find-length-of-list/
# ref: https://www.youtube.com/watch?v=T8UTagpN2mc
# ref: https://www.youtube.com/watch?v=Uh2ebFW8OYM
# ref: https://stackoverflow.com/questions/13730107/writelines-writes-lines-without-newline-just-fills-the-file
# ref: https://stackoverflow.com/questions/22456274/how-to-completely-remove-n-in-text-file-using-python
