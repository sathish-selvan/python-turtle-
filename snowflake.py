import turtle
sat = turtle.Turtle()
a=100
sat.speed(100)
def flake(distance):
    if distance > 1:
        sat.pensize(distance/10)
        sat.forward(distance)
        sat.backward(distance*(40/100))
        sat.left(45)
        flake(distance*(30/100))
        sat.right(45*2)
        flake(distance*(30/100))
        sat.left(45)
        sat.backward(distance*(60/100))
for i in range(1,9):
    sat.pencolor('#2aaac7')
    
    flake(100)
    sat.left(45)

sat.hideturtle()
    










turtle.done()