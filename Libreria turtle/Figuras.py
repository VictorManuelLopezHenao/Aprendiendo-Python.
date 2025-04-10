import turtle

# Crear una instancia de la tortuga
tortuga = turtle.Turtle()

# Configurar la velocidad de la tortuga (0 es la más rápida)
tortuga.speed(1)

# Configurar el color de la tortuga
tortuga.color("Blue")

# Configurar el grosor del lápiz
tortuga.pensize(3)

# Cambiar el color de fondo del lienzo
turtle.bgcolor("lightyellow")

# Cambiar la forma de la tortuga
tortuga.shape("turtle")

# Levantar el lápiz para mover la tortuga sin dibujar
tortuga.penup()
tortuga.goto(-100, 0)  # Mover a una nueva posición
tortuga.pendown()  # Bajar el lápiz para empezar a dibujar

# Dibujar un cuadrado
for _ in range(4):
    tortuga.forward(100)  # Mover hacia adelante 100 unidades
    tortuga.left(90)      # Girar 90 grados a la izquierda

# Cambiar el color de la tortuga
tortuga.color("Red")

# Dibujar un triángulo
for _ in range(3):
    tortuga.forward(100)  # Mover hacia adelante 100 unidades
    tortuga.left(120)     # Girar 120 grados a la izquierda

# Cambiar el color de la tortuga
tortuga.color("Green")

# Dibujar un círculo
tortuga.circle(50)  # Dibujar un círculo con radio 50

# Levantar el lápiz y mover la tortuga a una nueva posición
tortuga.penup()
tortuga.goto(100, 100)
tortuga.pendown()

# Dibujar una estrella
for _ in range(5):
    tortuga.forward(100)  # Mover hacia adelante 100 unidades
    tortuga.right(144)    # Girar 144 grados a la derecha

# Dejar una copia de la tortuga en su posición actual
tortuga.stamp()

# Escribir texto en la posición actual de la tortuga
tortuga.write("Estrella", move=False, align="center", font=("Arial", 12, "normal"))

# Dibujar y rellenar un círculo
tortuga.color("Purple")
tortuga.penup()
tortuga.goto(0, -50)
tortuga.pendown()
tortuga.begin_fill()
tortuga.circle(50)
tortuga.end_fill()

# Ocultar la tortuga después de dibujar
tortuga.hideturtle()

# Mantener la ventana abierta
turtle.done()