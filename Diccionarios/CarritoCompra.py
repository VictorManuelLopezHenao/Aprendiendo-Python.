print("\nCarrito de compras")

carrito = {}

def mostrar_menu():
    print("\n1. Agregar productos al carrito")
    print("2. Terminar")
    print("3. Salir")

while True:  #menu
    mostrar_menu()

    opc = int(input("\nElige una opcion: "))
   
    total = 0

    if opc == 1:
        producto = input("\nProducto: ")
        precio = float(input("Precio: "))
        carrito[producto] = precio
    
    elif opc == 2:
        total += precio
        for producto,precio in carrito.items():   #recorre los items del carrito
            print(f"\n{producto} {precio}")
        print(f"\nTotal = {total}")
        
    elif opc == 3:
        print("Gracias por visitar")
        break
    else:
        print("\nOpcion no valida")



