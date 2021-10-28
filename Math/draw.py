from turtle import *
def draw_triangle():
    reset()
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)
    left(120)
def draw_square():
    reset()
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
def draw_square(size):
    reset()
    for n in range(4):
        forward(size)
        right(90)
draw_square(75)
draw_square(150)
def rect_area():
    x = input()
    y = input()
    area = x * y
    return area
draw_triangle()
draw_square()
Draw_square(150)
rect_area()

