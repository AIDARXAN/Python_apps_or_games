from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)
for step in range(15):
    
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

a = Turtle()
a.color('red')
a.shape('turtle')

a.penup()
a.goto(-160, 100)
a.pendown()

b = Turtle()
b.color('blue')
b.shape('turtle')

b.penup()
b.goto(-160, 70)
b.pendown()

c = Turtle()
c.color('green')
c.shape('turtle')
c.penup()
c.goto(-160, 40)
c.pendown()

d = Turtle()
d.color('yellow')
d.shape('turtle')
d.penup()
d.goto(-160, 10)
d.pendown()

for turn in range(100):
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))

