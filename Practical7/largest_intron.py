'''
se regular expression to find all substrings that start with "GT" and end with "AG"
# The pattern 'GT\w+AG' matches any substring starting with GT, followed by one or more word characters (A, T, C, G), ending with AG
Initialize variable to store the length of the largest intron found
Iterate through each matched intron
Calculate the length of the current intron
Update the largest intron length if the current intron is longer
'''

# DNA sequence to analyze
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# Import the regular expression module to find patterns in the sequence
import re

# Use regular expression to find all substrings that start with "GT" and end with "AG"
# The pattern 'GT\w+AG' matches any substring starting with GT, followed by one or more word characters (A, T, C, G), ending with AG
intron_matches = re.findall(r'GT\w+AG', seq)

# Initialize the variable to store the length of the largest intron found
largest_intron_length = 0

# Check if any introns were found
if intron_matches:
    # Iterate through each matched intron
    for intron in intron_matches:
        # Calculate the length of the current intron
        current_length = len(intron)
        # Update the largest intron length if the current intron is longer
        if current_length > largest_intron_length:
            largest_intron_length = current_length
else:
    # If no introns were found, print a message
    print("No introns matching the GT...AG pattern were found.")

# Print the result
print(f"The length of the largest intron is: {largest_intron_length}")