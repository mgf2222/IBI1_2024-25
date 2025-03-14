'''
Pseudocode
1. Prompt the user to enter their weight in kilograms and convert it to a float, store in variable weight
2. Prompt the user to enter their height in meters and convert it to a float, store in variable height
3. Calculate the BMI using the formula: BMI = weight / (height * height), store result in variable bmi
4. Determine the weight category based on BMI value:
   a. If bmi < 18.5, set category to "underweight"
   b. If 18.5 ≤ bmi ≤ 30, set category to "normal weight"
   c. If bmi > 30, set category to "obese"
5. Print the result using a formatted string that includes the BMI value and weight category
'''
# Get the person's weight in kilograms from user input and convert it to a float
weight = float(input("Enter weight in kilograms: "))

# Get the person's height in meters from user input and convert it to a float
height = float(input("Enter height in meters: "))

# Calculate the BMI using the formula: BMI = weight / (height^2)
bmi = weight / (height ** 2) 

# Determine the weight category based on the BMI value
if bmi < 18.5:
    # If BMI is less than 18.5, the person is considered underweight
    category = "underweight"
elif 18.5 <= bmi <= 30:
    # If BMI is between 18.5 and 30, the person is considered normal weight
    category = "normal weight"
else:
    # If BMI is greater than 30, the person is considered obese
    category = "obese"   

# Print the result using an f-string to include the BMI value and weight category
print(f"Your BMI is {bmi}, which means you are considered {category}.")