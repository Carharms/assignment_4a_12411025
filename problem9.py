# Problem 9 - Text Analysis
# Author - Carter Harms

# Create empty list to place common_words text into

# import Counter function
from collections import Counter

words = list()
    # Read through common_words.txt file
f_contents = open("common_words.txt", 'r')
with open ("common_words.txt") as fin:
    for line in fin:
        # Create list of words and strip whitespace characters
         words.append(line.strip())

# ref 1
# Open speech.txt file with utf-8 encoding
f = open('speech.txt', 'r', encoding='utf-8')

# Read speech and turn all words to lowercase for analysis
entire_file = f.read()
entire_file = entire_file.lower()

# Create empty string for the abridged speech.txt
dream_speech_abridged = ''

# Remove common words from the dream speech
for word in entire_file.split():
     if word not in words:
            dream_speech_abridged += word + " "

# Count the frequency of each word
word_counts = Counter(dream_speech_abridged.split())
# Remove the i, it was lowered and I is the only capitalized character in the common_words.txt file
word_counts.pop('i')
# ref 2
# Create a dictionary of the 20 most common words in the dream_speech_abridged
most_common_words = word_counts.most_common(20)

# Create proper formatting for outputting the most common 20 words in the MLK "I Have A Dream Speech"
for key, value in most_common_words:
     print(f"{key}: {value}")


# Footnote Reference
# 1. ref: https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-posit
# 2. ref: https://stackoverflow.com/questions/26242494/counting-the-number-of-times-a-word-appears-in-a-string





# Open speech.txt
dream_speech = ()
f = open("speech.txt", 'r', encoding='utf-8')
for line in f:
     # Create list of words and strip whitespace characters
    line.strip().lower()

print(f)




# ref: https://stackoverflow.com/questions/44319712/python-removing-spaces-from-file-output-stripping-white-space

# Remove common words from the speech

#filtered_speech = []

#for item in dream_speech:
      #if item not in common_words:
            #filtered_speech.append(item)


            

#for element in speech_line:
    #if element 


# Count the frequency of each word

# Create a list of the 20 most frequent words


# ref: https://stackoverflow.com/questions/44319712/python-removing-spaces-from-file-output-stripping-white-space
