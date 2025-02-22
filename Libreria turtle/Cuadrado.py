import turtle

tortuga = turtle.Turtle()

tortuga.speed(0)   #velocidad maxima
tortuga.color("Blue")

len = 100

tortuga.forward(len)  #mueve hacia adelante 
tortuga.left(90)     #en left o right el valor es respecto a un angulo
tortuga.forward(len)
tortuga.left(90)
tortuga.forward(len)
tortuga.left(90)
tortuga.forward(len)



tortuga.hideturtle()  #oculta la tortuga despues de dibujar 
turtle.done()  #Mantiene la ventana abierta 