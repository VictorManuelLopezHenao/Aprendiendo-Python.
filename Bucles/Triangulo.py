print("\nTriangulo respecto a un numero")

num = int(input("\nDigite un numero: "))

for i in range(1, num + 1, 2):  #incrementar de 2 en 2 para nums impares
    for j in range(i, 0, -2): # Decrementar de 2 en 2 para obtener la secuencia descendente
        print(j, end=" ")
    print() # Nueva línea después de cada fila
