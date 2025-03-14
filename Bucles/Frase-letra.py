print("\nFrase - letra")

frase = input("Digite una frase: ")
letra = input("Digite una letra: ")
count = 0

for i in frase:
    if(letra == i):
        count = count + 1
        
print(f"Las veces que la letra {letra} se repite en la frase {frase} es: {count}")