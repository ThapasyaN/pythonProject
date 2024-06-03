# steps:
# 1.if(a number is not clearly divisible by 4 and has a remainder)
# it's not a leap year
# 2.else(if it's not clearly divisible 100)
# it's a leap year
# 3.else (if it's not clearly divisible by 400)
# it's not a leap year
# else it's a leap year
num = int(input("enter any year-\n"))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print("its a leap year")
        else:
            print("its not a leap year")
    else:
        print("its a leap year")
else:
    print("its not a leap year")

