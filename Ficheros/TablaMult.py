print("\nTabla Mult")

n = int(input("Digite un numero del 1 al 10: "))

def func(n):
    with open("TablaMult.txt", "w") as f:
        for i in range (1,11):
            f.write(f"\n{n} x {i} = {n * i}")


    with open("TablaMult.txt", "r") as f:
        print(f.read())

func(n)
