import turtle
sat = turtle.Turtle()
sat.penup()
sat.goto(0,-200)
sat.pendown()
sat.speed(0)
def dragoncurve(l,n):
    def x(n):
        if n == 0:
            return

        x(n-1)
        sat.right(90)
        y(n-1)
        sat.forward(l)

    def y(n):
        if n==0:
            return

        sat.forward(l)
        x(n-1)
        sat.left(90)
        y(n-1)

    turtle.forward(l)
    x(n)


dragoncurve(3,29)

turtle.done()