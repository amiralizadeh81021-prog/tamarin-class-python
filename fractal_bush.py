import turtle
import random

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.color("brown")

turtle.tracer(0, 0)

x = 0.0
y = 0.0
scale = 250 

for _ in range(50000):
    px = x * scale
    py = y * scale - 250
    
    t.goto(px, py)
    t.dot(2)

    r = random.random()
    if r < 0.1:
        nx, ny = x * 0.05, y * 0.6
    elif r < 0.2:
        nx, ny = x * 0.05, y * -0.5 + 1.0
    elif r < 0.6:
        nx, ny = x * 0.46 - y * 0.32, x * 0.39 + y * 0.38 + 0.6
    else:
        nx, ny = x * 0.47 - y * 0.15, x * 0.17 + y * 0.42 + 1.1
    
    x, y = nx, ny

turtle.update()
turtle.done()