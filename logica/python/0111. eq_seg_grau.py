print("Equação do segundo grau")
valA = float (input("Informe o valor de a: "))
valB = float (input("Informe o valor de b: "))
valC = float (input("Informe o valor de c: "))
print("Sua equação é:", valA, "x2 +", valB, "x +", valC, " = 0")
delta = float ((valB) ** 2 - 4 * valA * valC)
print ("O valor de delta é ", delta)

if delta < 0:
    print("Para delta negativo, não existem raizes reais")
elif delta == 0:
        raizQ = delta ** (1 / 2)
        x1 = float (-(valB) + (raizQ)) / (2 * (valA))
        print("Para delta zero, temos duas raizes iguais a: ", x1)
else:
    raizQ = delta ** (1 / 2)
    x1 = float (-(valB) + (raizQ)) / (2 * (valA))
    x2 = float (-(valB) - (raizQ)) / (2 * (valA))

    print("Para delta positivo. Raizes diferentes: ")
    print(f"x' = {x1:.2f}")
    print(f"x'' = {x2:.2f}") 