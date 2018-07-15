import random
import turtle
a = turtle.Pen()

a.shape("turtle")
a.width(3)
a.speed(0)

colorlist = ["red" , "green" , "blue" , "orange" , "yellow"]

def hexagon(size):
    for i in range(6):
        a.forward(size)
        a.left(60)

def square(size):
    for i in range(4):
        a.forward(size)
        a.left(90)

def line(size):
    for i in range(4):
        a.forward(size)
        a.left(10000000000009)

def triangle(size):
    for i in range(3):
        a.forward(size)
        a.left(120)

def star(size):
    for i in range(5):
        a.forward(size)
        a.left(216)

for i in range(100):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    a.up()
    a.goto(x, y)
    a.down()
    col = random.choice(colorlist)
    a.color(col)
    star(random.randrange(10, 217))
    line(random.randrange(10, 217))
    hexagon(random.randrange(10, 217))
    square(random.randrange(10, 217))
    triangle(random.randrange(10, 217))
