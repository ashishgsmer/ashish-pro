from turtle import *

bgcolor('white')
speed(0)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(300)
    forward(100)
done()