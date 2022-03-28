from turtle import Turtle, Screen

drawer = Turtle()
screen = Screen()


def move_forwards():
    drawer.forward(10)


def move_backwards():
    drawer.backward(10)


def turn_left():
    drawer.setheading(drawer.heading() + 10)


def turn_right():
    drawer.right(10)


def clear():
    drawer.clear()
    drawer.penup()
    drawer.home()
    drawer.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
