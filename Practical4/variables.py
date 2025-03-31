# Assign the value 15 to variable a
a = 15

# Assign the value 75 to variable b
b = 75

# Calculate the sum of a and b, and assign the result to variable c
c = a + b  # c will be 15 + 75 = 90

# Assign the value 90 to variable d
d = 90

# Assign the value 5 to variable e
e = 5

# Calculate the sum of d and e, and assign the result to variable f
f = d + e  # f will be 90 + 5 = 95

# Check if c is greater than e
if c > e:
    # If c is greater than e, print this message
    print("The c is longer.")
else:
    # If c is not greater than e, print this message
    print("The e is longer.")
# Since c is 90 and e is 5, c > e is True, so "The c is longer." will be printed

# Check if c is greater than f
if c > f:
    # If c is greater than f, print this message
    print("The bus commute is quicker.")
else:
    # If c is not greater than f, print this message
    print("The car commute is quicker.")
# Since c is 90 and f is 95, c > f is False, so "The car commute is quicker." will be printed
# The car commute is quicker because f (95 minutes) is less than c (90 minutes)

# Boolean variables

# Initialize variables X and Y
X = True
Y = False

# Create variable W which is 'both X and Y'
W = X and Y

# Truth table for W (X AND Y)
"""
X   |   Y   |   W
True | True | True
True | False| False
False| True | False
False| False| False
"""

