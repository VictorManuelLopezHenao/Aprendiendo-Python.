print("\nElimina las letras en las posc de los multiplos del 3 en un abc")

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nueva_lista = []

for i in range(len(lista)): #len = longitud de la cadena
    if((i+1) % 3 != 0):
        nueva_lista.append(lista[i]) #append agrega un elemento al final de la lista
print(nueva_lista)