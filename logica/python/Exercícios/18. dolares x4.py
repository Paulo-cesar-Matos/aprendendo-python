conver = int (input("Quantas conversões serão realizadas? "))
c = 1
while c <= conver:
    reais = float (input("Quantos reais você tem? R$"))
    dolares = reais / 5.11 
    print(f"Você vai ter US${dolares:.2f} dolares!")
    c = c + 1



# baseado na cotação de 23/09/2026
