import time

print("Contador")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
print("Contando")
conte = 1
if inicio <= fim:
    while inicio <= fim:
        print(f"{inicio}")
        inicio += 1
        time.sleep(conte)
elif inicio >= fim:
    while inicio >= fim:
        print(f"{inicio}")
        inicio -= 1
        time.sleep(conte)
