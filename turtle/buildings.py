import turtle as t
import random as r

screen = t.Screen()
screen.bgcolor("midnightblue")
t.hideturtle()
t.speed(0)


def get_screen_info():
    width = screen.window_width()
    height = screen.window_height()
    left = -width / 2
    right = width / 2
    top = height / 2
    bottom = -height / 2
    center_x = 0
    center_y = 0
    return {
        "width": width, "height": height, "left": left, "right": right,
        "top": top, "bottom": bottom, "center_x": center_x, "center_y": center_y
    }

def get_city_info(screen_info, margin, buildings_count):
    city_left = screen_info["left"] + margin
    city_right = screen_info["right"] - margin
    city_bottom = screen_info["bottom"]

    city_width = city_right - city_left
    building_width = city_width / buildings_count
    max_building_height = int(screen_info["height"] * 0.6)
    return {
        "left": city_left, "right": city_right, "bottom": city_bottom,
        "width": city_width, "building_width": building_width, "max_building_height": max_building_height
    }

def draw_star(x, y):
    t.color("yellow")
    t.penup()
    d = r.randint(1, 5)
    t.goto(x, y)
    t.dot(d)
    t.pendown()

def draw_stars(screen_info):
    count_stars =100
    for i in range(count_stars):
        x = r.randint(int(screen_info["left"]), int(screen_info["right"]))
        y = r.randint(int(screen_info["bottom"]), int(screen_info["top"]))
        draw_star(x, y)


def draw_building(x, bottom, width, height):
    t.penup()
    t.goto(x, bottom)
    t.pendown()
    t.color("grey")
    t.begin_fill()
    t.setheading(90)
    for i in [height, width, height, width]:
        t.forward(i)
        t.right(90)
    t.end_fill()

def draw_window(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.setheading(90)
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_windows_in_building(x, bottom, width, height):
    window_size = width / 5
    margin_x = width / 6
    margin_y = width / 7
    gap = width - 2 * margin_x - 2 * window_size
    window_1_x = x + margin_x
    window_2_x = x + margin_x + window_size + gap
    window_y = bottom + margin_y
    while window_y + window_size < bottom + height:
        if r.randint(0, 1) == 1:
            draw_window(window_1_x, window_y, window_size)
        if r.randint(0, 1) == 1:
            draw_window(window_2_x, window_y, window_size)
        window_y += window_size + margin_y



def build_city():
    screen_info = get_screen_info()
    buildings_count = 5
    draw_stars(screen_info)
    city_info = get_city_info(screen_info, 30, buildings_count)
    for i in range(buildings_count):
        x = city_info["left"] + i * city_info["building_width"]
        min_height = city_info["max_building_height"] // 3
        building_height = r.randint(min_height, city_info["max_building_height"])
        draw_building(x, city_info["bottom"], city_info["building_width"], building_height)
        draw_windows_in_building(x, city_info["bottom"], city_info["building_width"], building_height)

    t.done()


if __name__ == '__main__':
    build_city()