print("Escola Chico Butico") #entendedores entenderão
print("Calcular média de nota")
nota1 = int (input("Primeira nota: "))
nota2 = int (input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é: {media}")
if media >= 7:
    print("Passou!")
elif media >=5 or media < 7: # adicionado agora
    print("Ficou em recuperação :-(")
else:
    print("Reprovou :-(")