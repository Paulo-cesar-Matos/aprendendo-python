# import time
cont = 1
soma = 0
maior = None

while cont <= 5:
    n = int(input(f"Digite o {cont}º valor: "))

    if maior is None or n > maior:
        maior = n

    soma += n
    cont += 1

print(f"A soma de todos os valores foi {soma}")
print(f"O maior número foi {maior}")