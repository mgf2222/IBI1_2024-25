weight = float (input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2) 
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi <= 30:
    category = "normal weight"
else:
    category = "obese"   
print(f"Your BMI is {bmi}, which means you are considered {category}.")