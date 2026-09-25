# import time
cont = int(input("Digite um número: "))
soma = 1
maior = cont
while soma <= cont:
    print(f"somando com {soma}")
    soma += cont
    if cont > maior:
        maior = cont
    cont +=1
print(f"Soma tudo: {soma}")
print(f"Maior número da contagem: {maior}")

"""import time
cont = int (input("Digite um número: "))
cont = 1
soma = 0 
maior = cont
while cont <= 10:
    print(f"somando com {cont}")
    soma += cont
    cont += 1
    if cont > maior:
        maior = cont 
    
    time.sleep(1)
print(f"Soma tudo: {soma}")
print(f"Maior número: {maior}")
# sou muito cabeção mesmo de ter feito a mesma coisa do 15° exercício :|"""