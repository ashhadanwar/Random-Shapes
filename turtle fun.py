import random
import turtle
a = turtle.Pen()

a.shape("turtle")
a.width(3)
a.speed(0)

colorlist = ["red" , "green" , "blue" , "orange" , "yellow", "blue", "dark blue", "light blue", "black"]

def square(size):
    for i in range(4):
        a.forward(size)
        a.left(90)

for i in range(100000000000000):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    a.up()
    a.goto(x, y)
    a.down()
    col = random.choice(colorlist)
    a.color(col)
    square(random.randrange(10, 200))
