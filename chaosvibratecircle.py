import turtle

sat = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
sat.color('green')
sat.speed(0)
sat.penup()
sat.goto(0,200)
sat.pendown()

a = 0
b = 0
while True:
    sat.forward(a)
    sat.right(b)
    a+= 3
    b+=1
    if b == 360:
        break

sat.hideturtle()

turtle.done()