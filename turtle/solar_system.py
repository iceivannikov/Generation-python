import turtle as t

ZOOM = 0.2
PITCH = 18

planets = (
    ('Солнце', 1390, 'yellow'),
    ('Меркурий', 4.8794, '#8A8784'),
    ('Венера', 12.1036, '#D08824'),
    ('Земля', 12.742, '#6082CA'),
    ('Марс', 6.78, '#BF9A76'),
    ('Юпитер', 139.822, '#BAB9C3'),
    ('Сатурн', 116.464, '#D9AB47'),
    ('Уран', 50.724, '#60BDEE'),
    ('Нептун', 49.244, '#4C6DED'),
    ('Плутон', 2.3766, '#5B5D5A')
)

screen = t.Screen()
screen.setup(1000, 400)


def draw_circle(center_x, center_y, radius, color):
    t.penup()
    t.goto(center_x, center_y - radius)
    t.pendown()

    t.color('black', color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_name(name, center_x, center_y, radius):
    t.penup()
    t.goto(center_x, center_y - radius - 20)
    t.pendown()

    t.write(name, align='center')


def draw_planet(name, diameter, color, center_x, center_y):
    radius = diameter * ZOOM / 2

    draw_circle(center_x, center_y, radius, color)
    draw_name(name, center_x, center_y, radius)

    return center_x + radius + PITCH


def play():
    t.speed(0)
    t.hideturtle()

    x = -screen.window_width() / 2 + PITCH
    y = 0

    for name, diameter, color in planets:
        radius = diameter * ZOOM / 2

        x += radius
        x = draw_planet(name, diameter, color, x, y)

    t.done()


if __name__ == '__main__':
    play()