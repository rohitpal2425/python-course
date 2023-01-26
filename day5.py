#BMI stands for Body Mass Index
# print("\tThis is th BMI calculator")
height=float(input("Enter your height in meter: "))
weight=float(input("Enter your weight in kg: "))
BMI=round((weight/(height**2)),2)
if BMI <=18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight")
elif BMI <35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")