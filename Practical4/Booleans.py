# Boolean variables

# Initialize X as True and Y as False
X = True
Y = False

# Create a new variable W which is 'both X and Y' (logical AND)
W = X and Y

# Print the truth table for W
print("Truth table for W:")
print("X | Y | W")
print(f"T | T | {W if X and Y else 'F'}")
print(f"T | F | {W if X and not Y else 'F'}")
print(f"F | T | {W if not X and Y else 'F'}")
print(f"F | F | {W if not X and not Y else 'F'}")

