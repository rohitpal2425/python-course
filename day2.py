# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("Enter your age\n")
years = (90-int(age))
months = years*12
weeks= years*52
days = years*365
hours=years*8660
print(f"You have {days} days,{weeks} weeks, {months} months and {hours} hours left")