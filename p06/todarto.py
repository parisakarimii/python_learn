import turtle
t = turtle.Turtle()

length = 20
for i in range(20):
    t.forward(length)
    t.right(90)
    length += 10
    
turtle.done()
input()