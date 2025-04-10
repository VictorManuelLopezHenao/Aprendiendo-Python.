print("Retorna cuadrados")

entrada = (input("\nDigite una lista de numeros: "))
lista = [int(x) for x in entrada.split(" ")]  #ingresar nums enteros en una lista separados por un espacio

def cuadrados(lista):
    resultado = []
    for i in lista:
        resultado.append(i**2) #** eleva
    return resultado
    
print(cuadrados(lista))