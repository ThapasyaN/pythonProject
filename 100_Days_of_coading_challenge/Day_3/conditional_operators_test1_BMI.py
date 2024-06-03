print("To calculate the BMI of yours.")
weight = int(input("What is your weight in kg?\n"))
height = int(input("what is your height in m\n"))
BMI = int(weight / height ** 2)
if BMI < 18.28:
    print(f"your bmi is {BMI},you are under weight")
elif BMI < 25:
    print(f"your bmi is {BMI},your weight is normal")
elif BMI < 28.50:
    print(f"your bmi is {BMI},your slightly overweight")
elif BMI < 32.56:
    print(f"your bmi is {BMI},your obese")
else:
    print(f"your bmi is {BMI},you are clinically obese")

