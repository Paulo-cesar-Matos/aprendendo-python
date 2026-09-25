import time
cont = int(input("Escolha um valor para a contagem "))
cont2 = cont
inicio = 1
while inicio <= cont:
    print(f"Toma mais {inicio}")
    inicio += 1
    time.sleep(1)
print("Todo cuspido")
time.sleep(3)
while cont2 > 0:
    print(f"Chupando o cuspe {cont2}")
    cont2 -= 1
    time.sleep(1)
print("Chupei tudo")
print("Ahhh")
time.sleep(1)