print("\n\tPizzeria Bella Napoli")

pizza = input("\n¿Desea pizza vegetariana?: ")

print("\n\nTodas las pizzas contienen Mozzarella y Tomate")

if(pizza == "si"):
    print("\n\tMenú\n\nIngredientes vegetarianos:\nPimiento\nTofu")
    opc = input("\nElija una opcion: ")
    print("\n\tPedido completo\n\nPizza vegetariana\n\nIngredientes:")
    print(f"Mozzarella\nTomate\n{opc}")
elif(pizza == "no"):
    print("\n\tMenú\n\nIngredientes no vegetarianos:\nPeperoni\nJamon\nSalmon")
    opc = input("\nElija una opcion: ")
    print("\n\tPedido completo\n\nPizza no vegetariana\n\nIngredientes:")
    print(f"Mozzarella\nTomate\n{opc}")
   