print("\n\tGrupo segun su nombre y sexo")
nombre = input("\nDigite su nombre: ")
sexo = input("Digite su sexo: ")

if((nombre[0] <= 'M' and sexo[0] == "F") or (nombre[0] >= 'N' and sexo[0] == "M")):
    print("\nSegun sus datos, usted pertenece al grupo A")
else:
    print("\nSegun sus datos, usted pertenece al grupo B")


