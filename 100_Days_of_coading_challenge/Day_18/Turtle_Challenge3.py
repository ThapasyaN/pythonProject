from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

color = ["cyan", "dark orange", "lawn green", "deep pink", "medium purple", "light coral", "yellow"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for num_of_shape_sides in range(3, 11):
    timmy.color(random.choice(color))
    draw_shape(num_of_shape_sides)

screen = Screen()
screen.exitonclick()
