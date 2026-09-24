n1 = int (input("Informe um número: "))
n2 = int (input("Informe outro número: "))
media = int (n1 + n2) / 2 # colocar o int para calculos precedentes, incluíndo nos input
# fórmula errada
media2 = int (n1) + (n2) / 2 # 
print(f"A média de {n1} com {n2} é de {media}!")
print(f"E a média de {n1} com {n2} da fórmula sem os parenteses é de {media2}!")