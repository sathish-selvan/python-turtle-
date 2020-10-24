import turtle

sat = turtle.Turtle()
sat.speed(0)
sat.color("red")
for i in range(180,0,-1):
    sat.left(140)
    sat.forward(i)
    sat.circle(-(i/2),200)
    sat.setheading(60)
    sat.circle(-(i/2),200)
    sat.forward(i)
    sat.setheading(0)

turtle.done()