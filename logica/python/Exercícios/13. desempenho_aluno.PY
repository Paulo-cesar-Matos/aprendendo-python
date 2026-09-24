print("Escola Chico Butico") #entendedores entenderão
print("Calcular média de nota")
nota1 = float (input("Primeira nota: "))
nota2 = float (input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é: {media:.2f}")

if media >= 2:
    print("A nota de desempenho do aluno é F")
elif media >=5 or media < 5.5: 
    print("A nota de desempenho do aluno é E")
elif media >=6 or media < 6.5:
    print("A nota de desempenho do aluno é D")
elif media >=7 or media < 7.5:
    print("A nota de desempenho do aluno é C")
elif media >=8 or media < 8.5:
    print("A nota de desempenho do aluno é B")
else:
    print("A nota de desempenho do aluno é A")


"""elif media >=9 or media < 10:
    print("O desempenho do aluno é A")"""