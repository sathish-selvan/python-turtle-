import turtle
import random

sat1 = turtle.Turtle()
sat2 = turtle.Turtle()
sat3 = turtle.Turtle()
sat4 = turtle.Turtle()
sat5 = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#9fe5f5")
tur = [sat1,sat2,sat3,sat4,sat5]
x = -200
for t in tur:

    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0,-100)
    x += random.randint(80,160) 
    t.goto(x,random.randint(-100,100))
    t.pendown()
    




def branch(tur,distance):
    if distance <20:
        tur.color("green")
        tur.stamp()
        tur.color("brown")
    if distance > 10:
        tur.pencolor("brown")
        tur.pensize(distance/10)
        angle=random.randint(22,30)
        shink = random.uniform(0.6,0.8)
        tur.forward(distance)
        tur.left(angle)
        branch(tur,distance*shink)
        tur.right(angle*2)
        branch(tur,distance*shink)
        tur.left(angle)
        tur.backward(distance)

for i in tur:
    branch(i,100)






turtle.done()