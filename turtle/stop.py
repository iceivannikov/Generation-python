import turtle as t

def draw_fig(side, color):
    count_side = 8
    t.penup()
    t.goto(-side / 2, -side)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(count_side):
        t.forward(side)
        t.left(360 / count_side)
    t.end_fill()

def print_stop():
    t.penup()
    t.goto(0, -15)
    t.pendown()
    t.color('white')
    t.write(
        "STOP",
        align="center",
        font=("Arial", 50, "bold")
    )


def draw_sign():
    t.speed(0)
    t.hideturtle()
    draw_fig(100, "black")
    draw_fig(95, "white")
    draw_fig(90, "red")
    print_stop()
    t.goto(0,0)
    t.dot(5, "blue")
    t.done()




if __name__ == '__main__':
    draw_sign()