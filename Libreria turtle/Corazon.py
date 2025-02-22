import turtle

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.color("red")

len = 20

tortuga.goto(2*len, 1*len)
tortuga.goto(4*len, 0*len)
tortuga.goto(5*len, -2*len)
tortuga.goto(4*len, -4*len)
tortuga.goto(1*len, -7*len)
tortuga.goto(0, -8*len)

tortuga.penup()
tortuga.goto(0, 0)
tortuga.pendown()

tortuga.goto(-2*len, 1*len)
tortuga.goto(-4*len, 0*len)
tortuga.goto(-5*len, -2*len)
tortuga.goto(-4*len, -4*len)
tortuga.goto(-1*len, -7*len)
tortuga.goto(0*len, -8*len)

tortuga.hideturtle()
turtle.done()