import turtle

sat=turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
sat.speed(0)
sat.pencolor('lime')
a = 350
sat.penup()
sat.goto(-a,0)
sat.pendown()

sat.forward(a)
sat.left(90)
sat.forward(a)
sat.backward(a)
sat.right(90)
sat.backward(a)
for i in range(10,a,10):
    sat.forward(10)
    sat.goto((0,i))
    sat.goto((-(a-i),0))
sat.forward(10)
sat.forward(a)
for i in range(10,a,10):
    sat.backward(10)
    sat.goto(0,i)
    sat.goto((a-i),0)
sat.backward(10)
sat.right(90)
sat.forward(a)
for i in range(10,a,10):
    sat.backward(10)
    sat.goto(i,0)
    sat.goto(0,-(a-i))

sat.backward(10)
sat.forward(a)
for i in range(10,a,10):
    sat.backward(10)
    sat.goto(-i,0)
    sat.goto(0,-(a-i))

sat.hideturtle()



turtle.done()