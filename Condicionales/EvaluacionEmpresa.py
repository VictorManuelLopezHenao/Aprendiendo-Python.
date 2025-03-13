print("\n\tEvaluacion a empleados")

print("\nRecuerde\n0.0 - Inaceptable\n0.4 - Aceptable\n0.6 o mas - Meritorio")
punt = float(input("\nDigite su puntuacion: "))

if(punt == 0.0):
    print(f"\nPuntuacion: {punt}\nNivel de rendimiento: Inaceptable\nDinero: 0.0")
elif(punt == 0.4):
    print(f"\nPuntuacion: {punt}\nNivel de rendimiento: Aceptable\nDinero: {punt * 2400}")
elif(punt >= 0.6):
    print(f"\nPuntuacion: {punt}\nNivel de rendimiento: Meritorio\nDinero: {punt * 2400}")
