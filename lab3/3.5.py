__author__ = 'student'
import turtle
turtle.shape('turtle')
for k in range(10):
    for i in range(4):
        turtle.forward(k*30)
        turtle.left(90)
    turtle.penup()
    turtle.backward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.pendown()



input()