a=input("Enter first number\n")
b=input("Enter second number\n")
y=print("Your Sum is:",int(a)+int(b))


y=input("Enter the year\n")
leap=int(y)
if(leap % 4==0) and (leap % 400 == 0) and (leap % 100 == 0):

    print("Its leap year\n")
else:
    print("Its not Leap year")
