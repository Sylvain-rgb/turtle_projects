import turtle

def stairs(size, nb):
    for i in range(0, nb):
        t.left(90)
        t.forward(size)
        t.right(90)
        t.forward(size)

t = turtle.Turtle()

stairs(30, 5)

turtle.done()