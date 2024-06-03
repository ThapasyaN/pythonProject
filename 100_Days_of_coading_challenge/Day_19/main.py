from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)


def move_left():
    timmy.left(10)


def move_right():
    timmy.right(10)


def move_backward():
    timmy.backward(10)


def to_clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="f", fun=move_forwards)
screen.onkey(key="l", fun=move_left)
screen.onkey(key="r", fun=move_right)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="c", fun=to_clear)

screen.exitonclick()
