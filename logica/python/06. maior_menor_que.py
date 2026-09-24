print("Maior, menor que ou igual a")
val_a = int(input("Digite algum número: "))
val_b = int(input("Digite algum outro número: "))

# mostrar todos os valores
print("------------------------")
print("----Todos os valores----")
print("------------------------")
print(f"O valor {val_a} é maior que {val_b}?            {val_a > val_b}")
print(f"O valor {val_a} é menor que {val_b}?            {val_a < val_b}")
print(f"O valor {val_a} é maior ou igual a {val_b}?     {val_a >= val_b}")
print(f"O valor {val_a} é menor ou igual a {val_b}?     {val_a <= val_b}")
print(f"O valor {val_a} é igual a {val_b}?              {val_a == val_b}")
print(f"O valor {val_a} é diferente a {val_b}?          {val_a != val_b}")


"""
if val_a > val_b :
    print(f"O {val_a} é maior que {val_b}!")
elif val_a < val_b :
    print(f"O {val_a} é menor que {val_b}!")
elif val_a >= val_b:
    print(f"O {val_a} é maior ou igual a {val_b}!")
elif val_a <= val_b:
    print(f"O {val_a} é menor ou igual a {val_b}!")
elif val_a == val_b:
    print(f"O {val_a} é igual a {val_b}!")
elif val_a != val_b:
    print(f"O {val_a} é diferente a {val_b}!")
else:
    print("Não foi informado nenhum número...")"""