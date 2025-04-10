print("\nBase de datos de un cliente")

def mostrar_menu():
    print("\n1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Lista de clientes")
    print("5. Lista de clientes preferentes")
    print("6. Salir")


clientes = {}

while True:
    
    mostrar_menu()
    opc = int(input("\nElija una opcion: "))


    if opc == 1:
        print("Ingrese los siguientes datos: ")
        id = input("ID: ")
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        tel = input("Telefono: ")
        correo = input("Correo: ")
        preferente = input("Es preferente? S/N: ")

        if preferente == 'S':
            clientes[id] = {
            'nombre': nombre, 'direccion': direccion, 'telefono': tel, 'correo': correo,'preferente': True
            }
        else:
            clientes[id] = {
            'nombre': nombre, 'direccion': direccion, 'telefono': tel, 'correo': correo,'preferente': False
            }
    
    elif opc == 2:
        idB = input("Ingrese el id del cliente: ")
        clientes.pop(idB) #eliminar o devolver un elemento de una lista o diccionario
    
    elif opc == 3:
        idB = input("Ingrese el id del cliente: ")
        print(clientes.get(idB))

    elif opc == 4:
        print(clientes)
    
    elif opc == 5:
        for id, datos in clientes.items():
            if datos['preferente']:
                print(f"Id: {id}\nNombre: {nombre}")
        
    elif opc == 6:
        print("Gracias por visitar")
        break

    else:
        print("Opcion no valida")






   
