print("\tTablas de multiplicar")
n = int(input("\nDigite un numero: "))

for i in range (1,11):
    print(f"{n} * {i} = {n * i}")   #f indica que se está utilizando un f-string
    