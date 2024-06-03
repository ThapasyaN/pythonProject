print("welcome to the worlds famous roller coaster ride")
age = int(input("Please enter your age-\n"))
height = int(input("Please enter your height in cm\n"))
bill = 0
if height > 120:
    print("you can have a ride in our coaster")
    if age <= 12:
        bill = 7
        print("you have to pay 7$ as your under set 1")
    elif age <= 18:
        bill = 10
        print("you have to pay 10$ as your under set 2")
    elif age > 18 and age <= 20:
        bill = 0
        print("its free")
    else:
        bill = 12
        print("you have to pay 12$ as your under set 3")
    photo = input("do you want to take a photo. s oo n\n")
    print("if s you need to pay extra 3$")
    if photo == 's':
        bill += 3
        print(f"your total bill is ${bill}")
    else:
        print("thank you have a nice ride")
else:
    print("Sorry, you are too short for this ride")
