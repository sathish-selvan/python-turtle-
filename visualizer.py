import turtle

sat = turtle.Turtle()
sat.speed(0)
sat.penup()
sat.goto(-100,0)
sat.pendown()
for colours in ["Violet","cyan","green","yellow","orange","red","blue","purple","white"]:
    sat.color(colours)
    for i in range(100):
        sat.forward(200)
        sat.left(125)
        

turtle.done()