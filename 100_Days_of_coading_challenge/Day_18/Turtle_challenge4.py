import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(15)

for _ in range(300):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
