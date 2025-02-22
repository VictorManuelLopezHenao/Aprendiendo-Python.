print("\n\tCalculadora basica")

def Pidedatos():
    a = int(input("\nIngrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    return a,b

while True:
    print("\nSeleccione una opcion")
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opc = int(input("\nOpcion: "))

    if opc == 1:
        a, b = Pidedatos()
        print(f"La suma es igual a: {a + b}")
    elif opc == 2:
        a, b = Pidedatos()
        print(f"La resta es igual a: {a - b}")
    elif opc == 3:
        a, b = Pidedatos()
        print(f"La multiplicacion es igual a: {a * b}")
    elif opc == 4:
        a, b = Pidedatos()
        print(f"La division es igual a:  {a / b}")
    elif opc == 5:
        print("Saliendo...")
        break
    else:
        print("Opcion invalida, intente de nuevo") 



