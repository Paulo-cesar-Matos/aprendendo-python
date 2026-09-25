print("Colégio da Cabeça de Cebola") # entendedores entenderão
alunos = int (input("quantos alunos tem na sala? "))
conte = 1
maiorNota = 0.0
melhorAluno = ""


while conte <= alunos:
    print(f"\nAluno {conte}")
    nome_aluno = input("Nome do aluno: ")
    nota = float (input(f"Nota do {nome_aluno}: "))
    if conte == 1 or nota > maiorNota:
        maiorNota = nota
        melhorAluno = nome_aluno
    conte += 1
print("\n"+"="*40)
print(f"O melhor aluno foi {melhorAluno} com a {maiorNota:.2f}")
print("\n"+"="*40)