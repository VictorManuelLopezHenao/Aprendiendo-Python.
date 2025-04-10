print("\nEjercicio 11")

cadena = input("Digite una frase: ")

diccionario = {}

def func1(cadena):
    for palabra in cadena.split():
        contador = cadena.count(palabra)
        diccionario[palabra] = contador
    
    palabra, contador in diccionario.items()
        
    return diccionario

def func2(diccionario):
    Masrepetida = max(diccionario, key = diccionario.get) #encontrar la clave con el valor maximo
    frecuencia = diccionario[Masrepetida]
    return Masrepetida, frecuencia

diccionario = func1(cadena) #llamado a las funciones
palabra, frecuencia = func2(diccionario)

print(f"\nPalabras mas repetida: {palabra}\nFrecuencia: {frecuencia}")
