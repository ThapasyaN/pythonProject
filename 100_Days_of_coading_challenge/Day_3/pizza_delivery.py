print('''                                              
8b,dPPYba,  88 888888888 888888888 ,adPPYYba,  
88P'    "8a 88      a8P"      a8P" ""     `Y8  
88       d8 88   ,d8P'     ,d8P'   ,adPPPPP88  
88b,   ,a8" 88 ,d8"      ,d8"      88,    ,88  
88`YbbdP"'  88 888888888 888888888 `"8bbdP"Y8  
88                                             
88                                      \n''')
print("welcome to python pizza delivery")
size = input("which size of pizza do you want? s m l\n")
bill = 0
if size == 's':
    bill = 10
    print("you have to pay 10$")
    extra_pepper = input("Do you want some extra pepper?s or n\n")
    if extra_pepper == 's':
        bill += 2

    else:
        print("thank you for your visit")
    extra_cheese = input("Do you want some extra cheese?s or n\n")
    if extra_cheese == 's':
        bill += 1
    print(f"your total bill is ${bill}")
elif size == 'm':
    bill = 14
    print("you have to pay 14$")
    extra_pepper = input("Do you want some extra pepper?s or n\n")
    if extra_pepper == 's':
        bill += 4
    else:
        print("thank you for your visit")
    extra_cheese = input("Do you want some extra cheese?s or n\n")
    if extra_cheese == 's':
        bill += 2
    print(f"your total bill is ${bill}")

else:
    bill = 16
    print("you have to pay 16$")
    extra_pepper = input("Do you want some extra pepper?s or n\n")
    if extra_pepper == 's':
        bill += 6
    else:
        print("thank you for your visit")
    extra_cheese = input("Do you want some extra cheese?s or n\n")
    if extra_cheese == 's':
        bill += 3
        print(f"your total bill is ${bill}")
