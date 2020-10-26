import turtle

sat = turtle.Turtle()
sat.penup()
sat.goto(0,200)
sat.pendown()

sat.speed(0)



for i in range(200,0,-1):
    sat.forward(i)
    sat.right(90)
    sat.forward(i)
    sat.right(90)
    sat.right(1)


for i in range(200,0,-1):
    sat.forward(i)
    sat.left(90)
    sat.forward(i)
    sat.left(90)
    sat.left(1)





turtle.done()




