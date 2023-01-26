print("Lets start Python Day 1")
a=input("Enter First Number\n" )
b=input("Enter Second Number\n" )
x=int(a)
y=int(b)
op=input("Enter operator:\n")
if(op=='+'):
    print("The Addition is:",x+y)
elif(op=='-'):
    print("The sbtraction is:",x-y)
elif(op=='*'):
    print("The multiplication is:",x*y)
elif(op=='/'):
    print("The division is:",x/y)
elif(op=='%'):
    print("The Modulo is:",x%y)
else:
    print("Invalid Operator")
    
