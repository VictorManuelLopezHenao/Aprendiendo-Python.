print("\nTraduccion español-ingles")

entrada = input("\nDigite la palabra de esta manera (español:ingles) : ")

diccionario = {}

pares = entrada.split(",") #divide los pares por comas

for par in pares:
    español, ingles = par.split(":")
    diccionario[español.strip()] = ingles.strip()   #strip para eliminar los espacios

for español, ingles in diccionario.items(): #recorre los items del dicc
    print(f"{español} -> {ingles}") 

frase = input("\nDigite una frase: ")

palabras = frase.split()
traduccion = []

for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra)) #get para obtener el valor de una clave, sin lanzar error si la clave no existe.

print("\nFrase traducida")
print(" ".join(traduccion)) #join para unir elementos de una lista en una sola cadena


