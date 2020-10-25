import turtle

sat = turtle.Turtle()
sat.speed(0)
lst = ["blue","yellow","brown","orange","red"]
for i in range(0,250):
    sat.color(lst[i%5])
    sat.pensize(i/10+1)
    sat.forward(i)
    sat.left(59)

turtle.done()