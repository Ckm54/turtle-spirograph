import turtle as t
import random

drawer = t.Turtle()
t.colormode(255)


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


drawer.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        drawer.color(get_color())
        drawer.circle(100)
        drawer.setheading(drawer.heading() + gap_size)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
