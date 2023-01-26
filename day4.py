# String Slicing
names="Rohit, Saroj"
# len1=(len(names))
print("Names is ", len(names), "letter word" )
print(names[0:4]) 
# including 0 but not including 4
fruit="Mango"
print(fruit[0:3])
# negagtive slicing
print(fruit[0:-2])
# it is same like
print(fruit[0:len(fruit)-2])
# Another way
print(fruit[-4:-2])
# it is also same like
print(fruit[len(fruit)-4:len(fruit)-2])