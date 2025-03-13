print("\n\tSala de videojuegos")

edad = int(input("\nIngrese su edad: "))

if(edad < 4):
    print(f"\nSu edad es {edad} y su entrada no tiene costo")
elif(edad >= 4 and edad <= 18):
    print(f"\nSu edad es {edad} y el valor de su entrada es de 5E")
elif(edad > 18):
    print(f"\nSu edad es {edad} y el valor de su entrada es de 10E")


