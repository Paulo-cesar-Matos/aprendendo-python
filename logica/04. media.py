n1 = int (input("Informe um número: "))
n2 = int (input("Informe outro número: "))
media = int (n1 + n2) / 2 # colocar o int para calculos precedentes, incluíndo nos input
# fórmula errada
media2 = int (n1) + (n2) / 2 # 
print(f"A média de {n1:.0f} com {n2:.0f} é de {media:.2f}!")
print(f"E a média de {n1:.0f} com {n2:.0f} da fórmula sem os parenteses é de {media2:.2f}!")