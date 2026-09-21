print("---------------------------------")
print("Depertamento de transito")
print("---------------------------------")
ano_atual = int (input("Ano atual (yyyy): "))
ano_nasc = int (input("Ano de nascimento (yyyy): "))
idade = ano_atual - ano_nasc
if idade >= 18:
    print("Pode")
else:
    print("Pode não man")