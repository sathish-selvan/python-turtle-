import turtle

sat = turtle.Turtle()
s = turtle.Screen()
lst = ["green","yellow","orange","red"]
sat.up()
sat.goto(200,0)

for i in range(0,4):
    sat.down()
    sat.begin_fill()
    sat.fillcolor(lst[i])
    sat.circle(50)
    sat.end_fill()
    sat.up()
    sat.bk(100)

turtle.done()
