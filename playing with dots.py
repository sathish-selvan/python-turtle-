import turtle
sat = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
sat.penup()
sat.goto(0,0)
sat.pendown()
sat.speed(0)
n = 10

for k in range(1,37):
        
    for i in range(5):
        sat.penup()
        sat.forward(50)
        sat.pendown()
        sat.dot(5*i)
    sat.penup()
    sat.goto(0,0)
    sat.pendown()
    sat.left(10)
sat.left(5)
sat.penup()
sat.goto(0,0)
sat.pendown()
sat.forward(25)
for k in range(1,37):
        
    for i in range(5):
        sat.penup()
        sat.forward(50)
        sat.pendown()
        sat.dot(5*(i+1))
    sat.penup()
    sat.goto(0,0)
    sat.pendown()
    sat.forward(25)
    sat.left(10)
    
sat.hideturtle()



turtle.done()