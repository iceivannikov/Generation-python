import turtle as tr
import math as m

tr.speed(0)
tr.hideturtle()

def draw_heart():
    tr.color("red")
    tr.begin_fill()
    t = 0
    while t <= m.pi * 2:
        x = 128 * m.sin(t) ** 3
        y = 8 * (13 * m.cos(t) - 5 * m.cos(2 * t) - 2 * m.cos(3 * t) - m.cos(4 * t) - 5)
        tr.goto(x, y)
        t += 0.01
    tr.end_fill()
    tr.done()

if __name__ == '__main__':
    draw_heart()