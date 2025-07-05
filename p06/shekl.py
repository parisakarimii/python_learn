import turtle


screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)


def draw_polygon_circle(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(size)
        pen.left(angle)


pen.penup()
pen.goto(0, 0)
pen.pendown()

for i in range(36):
    draw_polygon_circle(6, 100)  
    pen.right(10)


turtle.done()