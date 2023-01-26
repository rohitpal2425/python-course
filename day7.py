# String methods
# upper() :The upper() method converts a string to upper case.
a="Rohit Pal"
print(len(a))
print(a)
print(a.upper())


# lower():The lower() method converts a string to lower case.
b="SAROJ"
print(b.lower())
# strip() :The strip() method removes any white spaces before and after the string.
c="    Hello This is Python program     "
e="    Hello This is Python program     "
print(c.strip())
print(e)


# rstrip() :the rstrip() removes any trailing characters.
str1="Hy!!!!!!"
print(str1.rstrip("!"))


# replace() :The replace() method replaces all occurences of a string with another string.
str2="Rohit Sharma"
print(str2.replace("Sharma","Pal"))


# split() :The split() method splits the given string at the specified instance and returns the separated strings as list items.
str2="Rohit pal saroj pal xyz etc"
print(str2.split(' '))


# capitalize() :the first character of the string to uppercase
str2="hello every One "
str3=str2.capitalize()
print(str3)


# center() :Align centre
a="This is centre aligning"
print(a.center(75))
print(a.center(75,"-"))
print(a.center(75,"."))
print(a.center(75,":"))
print(a.center(75,"~"))
print(a.center(75,"*"))


# count() :it is used for count number of value is prenent in the string
a="hey harry how are you. Can you give me your mobile phone"
b=a.count("a")
c=a.count("e")
d=a.count("h")
print(b)
print(c)
print(d)


# endswith() :The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
a="hey harry how are you. Can you give me your mobile phone?"
print(a.endswith("?"))
print(a.endswith("."))
print(a.startswith("h"))
print(a.startswith("H"))


# find() :searches for the first occurrence of the given value and return
# s the index where it is present. 
r= "He's name is Dan. He is an honest man."
print(r.find("is"))
# If given value is absent from the string then return -1.
print(r.find("q1"))


# index() :searches for the first occurrence of the given value and returns the index where it is present.
p="Hey dear I love you"
print(p.index("love"))
# If given value is absent from the string then raise an exception.
# print(p.index("rohit"))


# isalnum() :returns True only if the entire string only consists of A-Z, a-z, 0-9.
a="I have 2 rupees money"
print(a.isalnum())
# Space matter in this 
a="Ihave2rupeesmoney"
print(a.isalnum())


# isalpha() :The isalnum() method returns True only if the entire string only consists of A-Z, a-z.
a="I have 2 rupees money"
print(a.isalpha())
a="iloveyou"
print(a.isalpha())


# islower() :The islower() method returns True if all the characters in the string are lower case, else it returns False.
a="Iloveyou"
print(a.islower())
a="iloveyou"
print(a.islower())
a="ILOVEYOU"
print(a.isupper())
a="ILOVEYOu"
print(a.isupper())


# isspace() :The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())


# istitle() :The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "world Health Organization" 
print(str1.istitle())


# swapcase() :The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Hello I Am ROhit Pal" 
print(str1.swapcase())
str1 = "hELLO I aM rOHIT pAl" 
print(str1.swapcase())