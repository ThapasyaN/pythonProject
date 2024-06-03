num_char = len(input("what is your name?"))
# >>Type conversion/Type casting: to change the data type

# 1.to change the int data type into a string so that it can be concatenated: str()
new_num_char = str(num_char)
print("to find the number of characters in the above given string")
print("your name has " + new_num_char + " characters")

# 2.to change the string data type into a float
a = float(3.14)
print("printing a number")
print(type(a))
print("adding  a float data type to an integer data type ")
print(1 + float("20.9"))
# >>in here first the string data type gets converted into a float and then it gets added

print("adding two string data typed numbers")
print(str(109) + str(2009))

# 3.to change the string data type into an integer data type: int()
print("printing a value")
a = '22'
print("checking the data type of the given value")
type(a)
print("changing the data type into an integer daa type")
new_a = int(a)

# 4.rounding of the value to the nearest value: round()
print("rounding of the value to the next nearest number")
print(round(3.4))
print(round(8 / 3))
# if you wanna round it to 2 decimal places u need to mention the number 2 eg:
print("rounding of the number to next nearest number by 2")
print(round(8 / 3, 2))  # then it prints 2 decimal places as mentioned
print(round(2.666666666, 2))  #  to print next 2 numbers after the decimal point

# float division // =  round()  >>they both are same
# if we use float division - no need to convert in into an integer
print(round(8 / 3))  #  or
print(8 // 3)
