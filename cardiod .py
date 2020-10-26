

import turtle

sat = turtle.Turtle()
s =turtle.Screen()
sat.pencolor("black")
s.bgcolor("#72cc12")
sat.penup()
sat.speed(0)
sat.goto(0,-300)
sat.pendown()


table = 2
points = []
division = 200

def draw(division):
    for i in range(division):
        points.append(sat.pos())
        sat.circle(300,360/division)


draw(division)

for i in points:
    sat.goto(i)
    sat.goto(points[(points.index(i)*table)%division])
    sat.goto(i)


sat.hideturtle()
turtle.done()
