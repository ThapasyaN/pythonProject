print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure island")
print("Your mission is to find the treasure")
direction = input("your at a cross road .Where do you want to go. Type 'left' or 'right'\n")
if direction == 'right':
    print("Game over. There is a tiger in your way.")
else:
    print("your near the lake. There is an island in the middle of the lake.")
    source = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if source == 'swim':
        print("Game over. there are crocodiles in the lake")
    else:
        print("you arrived at an island unharmed")
        door_colour = input("There is a house with 3 doors.One red, one yellow, and one blue. Which colour do you "
                            "choose?")
        if door_colour == "red":
            print("Game over. you entered in a room full of fire")
        elif door_colour == "blue":
            print("Game over. you entered in a room of beasts")
        else:
            print("You win!. you entered in a room of treasures")
