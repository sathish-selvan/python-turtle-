import turtle

sat = turtle.Turtle()
s = turtle.Screen()
sat.speed(0)
sat.penup()
sat.goto(0,-100)
sat.pendown()
s.bgcolor("black")
sat.color("green")
for d in range(0,12):
    for i in range(0,72):
        sat.forward(100)
        sat.left(90)
        sat.forward(100)
        sat.left(90)
        sat.forward(100)
        sat.left(90)
        sat.forward(100)
        sat.left(90)
        sat.left(5)
    sat.forward(70)
    sat.left(30)



turtle.done()
