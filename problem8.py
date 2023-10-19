# Problem 8 - DNA Sequencing
# Problem 8 - Complete

# Author: Carter Harms

# Import counter function for tallying elements of a list
from collections import Counter

# DNA sequence string
dna_sequence = '''
GTACGACGGAGTGTTATAAGATGGGAAATCGGATACCAGATGAAATTGTGGATCAGGTGCAAAAGTCGGC
AGATATCGTTGAAGTCATAGGTGATTATGTTCAATTAAAGAAGCAAGGCCGAAACTACTTTGGACTCTGT
CCTTTTCATGGAGAAAGCACACCTTCGTTTTCCGTATCGCCCGACAAACAGATTTTTCATTGCTTTGGCT
GCGGAGCGGGCGGCAATGTTTTCTCTTTTTTAAGGCAGATGGAAGGCTATTCTTTTGCCGAGTCGGTTTC
TCACCTTGCTGACAAATACCAAATTGATTTTCCAGATGATATAACAGTCCATTCCGGAGCCCGGCCAGAG
TCTTCTGGAGAACAAAAAATGGCTGAGGCACATGAGCTCCTGAAGAAATTTTACCATCATTTGTTAATAA
ATACAAAAGAAGGTCAAGAGGCACTGGATTATCTGCTTTCTAGGGGCTTTACGAAAGAGCTGATTAATGA
ATTTCAGATTGGCTATGCTCTTGATTCTTGGGACTTTATCACGAAATTCCTTGTAAAGAGGGGATTTAGT
GAGGCGCAAATGGAAAAAGCGGGTCTCCTGATCAGACGCGAAGACGGAAGCGGATATTTCGACCGCTTCA
GAAACCGTGTCATGTTTCCGATCCATGATCATCACGGGGCTGTTGTTGCTTTCTCAGGCAGGGCTCTTGG'''

# Transforming string into list
dna_list = list(dna_sequence)
# Creating dictionary of total characters assigned to each value
x = Counter(dna_list)
# Removing whitespace lines
x.pop('\n')

# Confirming total 
percentages = sum(x.values())
for key, num in x.items():
    pct = num * 100 / percentages
    pct = round(pct)

    print(f"{key}: {pct}%")

# Footnote references
# ref: https://stackoverflow.com/questions/70771697/find-character-occurance-percentage-from-a-list-of-words
# ref: https://stackoverflow.com/questions/73872639/how-to-extract-percentages-from-counter-function
