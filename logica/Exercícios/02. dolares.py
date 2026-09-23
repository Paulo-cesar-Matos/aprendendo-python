reais = float (input("Quantos reais você tem? R$"))
dolares = reais / 5.11 # baseado na cotação de 23/09/2026
print(f"Você vai ter US${dolares:.2f} dolares!") # o :.2f é para limitar a quantidade de digitos que o programa pode mostrar