l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))

tri = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)
eq = l1 == l2 and l2 == l3 
es = l1 != l2 and l2 != l3 and l1 != l3
iso = (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l1 != l2)

print(f"Pode formar um triangulo? {tri}")
print(f"O triangulo é EQUILATERO? {eq}")
print(f"O triangulo é ESCALENO? {es}")
print(f"O triangulo é ISÓSCELES? {iso}")