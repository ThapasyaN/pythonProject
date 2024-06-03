import random

rock = '''|__|   __|__|   __|__|   __|   
 __|__|   __|__|   __|__|   __|__|   _
|   __|__|   __|__|   __|__|   __|__| 
|__|   __|__|   __|__|   __|__|   __|_
 __|__|   __|__|   __|__|   __|__|   _
|   __|__|   __|__|   __|__|   __|__|   
|__|   __|__|   __|__|   __|__|   __|_
 __|__|   __|__|   __|__|   __|__|   _ 
|   __|__|   __|__|   __|__|   __|__|   \n'''

paper = ''' __________
         |DAILY NEWS|
         |&&& ======|
         |=== ======|
         |=== == %%$|
         |[_] ======|
         |=== ===!##|
         |__________|\n'''

scissors = '''' _    _
   (_)  / )
     | (_/ 
    _+/  
   //|*
  // | )
 (/  |/      '''

game_image = [rock, paper, scissors]
users_choice = int(input("What do you choose? Type 0 for rock , 1 for paper "
                         ", 2 for scissors\n"))
if users_choice >= 3 or users_choice < 0:
    print("you typed an invalid number. you lose!")
else:
    print(game_image[users_choice])

computer_choice = random.randint(0, 2)
print("computer chose=")
print(game_image[computer_choice])


if users_choice == 0 and computer_choice == 2:
    print("you win!")
elif users_choice > computer_choice:
    print("you win!")
elif computer_choice > users_choice:
    print("you lose!")
elif users_choice == computer_choice:
    print("it's a draw")

                        # or

    # if users_choice == 0 and computer_choice == 2:
    #     print("you win!")
    # elif users_choice == 0 and computer_choice == 1:
    #     print("you lose!")
    # elif users_choice == 1 and computer_choice == 2:
    #     print("you lose!")
    # elif users_choice == 1 and computer_choice == 0:
    #     print("you win")
    # elif users_choice == 2 and computer_choice == 0:
    #     print("you lose!")
    # elif users_choice == 2 and computer_choice == 1:
    #     print("you win!")
    # elif users_choice == computer_choice:
    #     print("it's a draw")
    # else:
    #     print("you typed an invalid number. you lose!")

