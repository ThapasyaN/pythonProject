print('''   _____           _____
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(              "              )8
I8                             8I
 Yb,                         ,dP
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        `Y8a         a8P'
          `88,     ,88'
            "8b   d8"  
             "8b d8"   
              `888'
                "
''')
name1 = input("enter the name-")
name2 = input("enter the name-")
combined_name = name1 + name2
lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
first_digit = t + r + u + e
print("the score of true is "+str(first_digit))

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
second_digit = l + o + v + e
print("the score of love is "+str(second_digit))

print("your love calculator is calculating your score....")
love_score =int(str(first_digit) + str(second_digit))

if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score} and you go together like coke amd mentos")
elif (love_score>=40) or (love_score <= 50):
    print(f"your love score is {love_score} and its all good to be together")
else:
    print(f"your love score is {love_score}")

