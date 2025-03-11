# 1. Initialize a variable to keep track of the current number (n)
# 2. For each number from 1 to 10:
#    a. Calculate the triangular number using the formula n*(n+1)/2
#    b. Print the result

# Initialize the starting value for n
n = 1

# Loop to calculate and display the first ten triangular numbers
while n <= 10:
    # Calculate triangular number using the formula
    triangular_number = n * (n + 1) // 2
    
    print(triangular_number)
    
    # Increment n for the next iteration
    n += 1