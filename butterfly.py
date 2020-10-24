import turtle

sat = turtle.Turtle()

sow = turtle.Turtle()
sow.speed(0)
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




