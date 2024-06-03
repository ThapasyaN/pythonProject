"""local scope: it exists within the functions
type_of_sport = "cricket"


def sports():
    drink_portion = 2
    print(type_of_sport)
print(drink_portion)
in this case the type_of_sport is not be printed and also the drink_portion as it's defined inside the function"""


"""Global scope: these variables are available both inside and outside the functions
strength = 10


def sports_person():
    drink_portion = 1
    print(strength)
in this case strength will be printed as it globally assigned and can be used anywhere in the program"""


# Modifying a Global scope
"""
enemies = 1


def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# instead of assigning the global variable as a local ones we can also use:
enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies += 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
"""


"""
Global constance:
PI = 3.14159
NAME = Thapasya
SO, it stores the values the we never wanted to change in the future circumstances, and is always in all_caps
"""
