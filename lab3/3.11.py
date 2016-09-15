__author__ = 'student'
import turtle
turtle.shape('turtle')
turtle.speed(1000)
for i in range (8):
    for j in range(361):
        turtle.forward(1+i/10)
        turtle.left(1)
    for c in range(361):
        turtle.forward(1)
        turtle.right(1)
