time1 = input("Qual o nome do time? ")
time2 = input("Qual o nome do outro time? ")
plac1 = int (input(f"Qual o placar de {time1}? "))
plac2 = int (input(f"Qual o placar de {time2}? "))

if plac1 > plac2:
    diferenca = plac1 - plac2
else:
    diferenca = plac2 - plac1

print(f"Diferença: {diferenca}")

match diferenca:
    case 0:
        print("Resultado: DEU VELHA")
    case 1 | 2 | 3:
        print(f"Resultado: Os torcedores de {time1} e {time2} fizeram tanta confusão que o estádio teve que ser demolido :|")
    case 4 | 5 | 6 | 7:
        print("Resultado: Eu fui lá e dei gol")
    case _:
        print("Result: You Reposted in the Wrong Neighborhood")
        print("Resultado: Você Repostou no Bairro Errado")