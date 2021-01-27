import turtle

def draw_square(size):
    for i in range(0, 4):
        t.forward(size)
        t.left(90)

t = turtle.Turtle()

draw_square(100)

turtle.done()