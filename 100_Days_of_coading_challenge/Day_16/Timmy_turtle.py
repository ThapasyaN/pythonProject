# import another_variable
#
# print(another_variable.variable)

import turtle
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon name", ["Charmender", "Squrtle", "Pikachu"])
# table.add_column("Type", ["Fire", "Water", "Electricity"])
# table.align = "l"
# print(table)
