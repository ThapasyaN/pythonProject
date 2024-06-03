num_char = len(input("what is your name?"))

# print("your name has" + num_char + "characters")
# >>TypeError: can only concatenate str (not "int") to str

# to check the type of data we used: type()
print(type(num_char))
print("converting it into a string data type so that it can be concatenated")
# type() is a type checking function

# >>Type conversion/Type casting: to change the data type

# 1.to change the int data type into a string so that it can be concatenated: str()
new_num_char=str(num_char)
print("your name has " + new_num_char + " characters")


