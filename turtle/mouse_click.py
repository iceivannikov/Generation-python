import turtle as t
import random as r


def random_color():
    return r.randrange(256), r.randrange(256), r.randrange(256)


def draw_star(x, y, size, points, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(r.randint(0, 360))
    for i in range(points):
        t.forward(size)
        t.right(180 - 180 / points)
    t.end_fill()


def left_mouse_click(x, y):
    size = r.randint(10, 50)
    points = r.randrange(5, 14, 2)
    color = random_color()
    draw_star(x, y, size, points, color)


screen = t.Screen()
screen.colormode(255)
screen.bgcolor("black")
t.hideturtle()
t.speed(5)

if __name__ == '__main__':
    screen.onclick(left_mouse_click)
    screen.listen()
    t.done()
