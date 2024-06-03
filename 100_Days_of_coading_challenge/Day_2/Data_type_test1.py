num = input("input a two digit number")
print("checking the type of data")
print(type(num))
print("converting the string data type into an integer data type")
#  >>you need to convert each digit into an integer data type
a = int(num[0])
b = int(num[1])
# >>you can't concatenate an integer data type so u need to convert it into a string data type for printing it
print("first digit= " + str(a))
print("second digit= " + str(b))
print("sum of digits= " + str(a + b))
