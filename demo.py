import turtle

sat = turtle.Turtle()
lst = ["green","yellow","brown","orange","red"]
for i in range(0,200):
    sat.color(lst[i%5])
    sat.pensize(i/10+1)
    sat.forward(i)
    sat.left(70)

turtle.done()