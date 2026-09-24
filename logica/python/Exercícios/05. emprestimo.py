emp = float(input("Qual o valor do emprestimo? R$"))
parcelas = int(input("Quantas parcelas? "))
total = (emp * 20) / 100
pagar = total / parcelas
print(f"Você irá pagar R${pagar:.2f} reais em suaves parcelas de {parcelas} vezes!")