__author__ = 'student'
import turtle
turtle.shape('turtle')
n=int(input())
for i in range(n):
    for k in range(n):
        turtle.forward(10)
    turtle.stamp()

    turtle.penup()
    turtle.goto(2,2)
    turtle.left(360//n)
    turtle.pendown()


