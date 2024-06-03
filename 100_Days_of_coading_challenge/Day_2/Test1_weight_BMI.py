# BMI = weight/height**2   formula

print("to check the BMI of " + input("What is your name?"))
weight = int(input("enter your weight in kg"))
height = float(input("enter your height in m"))
BMI = weight / height ** 2
# or BMI = weight / (height * height)
BMI_in_integer = int(BMI)
print("checking the data type of BMI\n" + str(type(BMI_in_integer)))
print("THE BMI OF YOURS IS= " + str(BMI_in_integer))
