print("\nAsignaturas reprobadas")

x = ["matematicas", "fisica", "quimica", "historia", "lengua"]

print(x)

notas = []

for i in range(5):
    nota = float(input("Digite las notas de cada materia respectivamente: "))
    notas.append(nota)

reprobadas = []

for i in range(5):
    if notas[i] < 3:
        reprobadas.append(x[i])

    

print(reprobadas)
