print("\nElimina las letras en las posc de los multiplos del 3 en un abc")

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nueva_lista = []

for i in range(len(lista)):
    if((i+1) % 3 != 0):
        nueva_lista.append(lista[i])
print(nueva_lista)