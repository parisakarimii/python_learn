import turtle
sun = turtle.Turtle()

for _ in range(12):
    sun.forward(150)
    sun.backward(150)
    sun.right(30)


sun.begin_fill()
sun.color("yellow")
sun.penup()
sun.goto(0, -100)
sun.pendown()
sun.circle(100)
sun.end_fill()

input()