nome = str(input("Qual o nome do funcionário? "))
salario = float(input("Qual o seu salário? R$"))
depende = int(input("Quantas pessoas dependem do seu salário? "))

if depende == 0:
    nsal = salario + (salario * 5/100)
elif depende in [2-4]:
    nsal = salario + (salario * 15/100)
elif depende in [5-7]:
    nsal = salario + (salario * 25/100)
elif depende in [8-25]:
    nsal = salario + (salario * 40/100)
else:
    nsal = salario + (salario * 80/100)

print(f"O novo salário de {nome} será de R${salario:.2f}. Mas o colaboardor deveria colocar todo mundo pra fora de casa pra criarem vergonha na cara e irem trabalhar...")