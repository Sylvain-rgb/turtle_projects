import turtle

def draw_squares(beginning_size, nb):
    for i in range(0, nb):
        size = (i+1)*beginning_size
        for z in range(0, 4):
            t.forward(size)
            t.left(90)

t = turtle.Turtle()

draw_squares(10, 10)

turtle.done()