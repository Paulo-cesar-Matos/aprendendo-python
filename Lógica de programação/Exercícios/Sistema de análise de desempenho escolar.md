### **Desafio: Sistema de Análise de Desempenho Escolar**

**Objetivo:** Criar um programa para analisar o desempenho de uma turma. O sistema deve armazenar os nomes dos alunos em um **vetor (lista)** e suas notas em diferentes disciplinas em uma **matriz** (onde cada linha representa um aluno e cada coluna representa uma disciplina).

---

### **Requisitos do Programa**

1. **`calcular_medias(matriz_notas)`**: Função que recebe a matriz de notas, calcula e retorna um **vetor** com a média de cada aluno.
2. **`maior_nota_disciplina(matriz_notas, indice_disciplina)`**: Função que recebe a matriz e o índice de uma disciplina (coluna), retornando a maior nota obtida nela.
3. **`exibir_relatorio(alunos, matriz_notas)`**: Função que calcula as médias e exibe um relatório formatado com o nome do aluno, suas notas, sua média final e a situação (**Aprovado** para média \(\ge 7.0\) ou **Reprovado**).

---

### **Código da Solução em Python**

```
# 1. Função para calcular a média de cada aluno (retorna um vetor/lista)
def calcular_medias(matriz_notas):
    medias = []
    for linha in matriz_notas:
        media_aluno = sum(linha) / len(linha)
        medias.append(media_aluno)
    return medias

# 2. Função para encontrar a maior nota de uma disciplina específica (coluna)
def maior_nota_disciplina(matriz_notas, indice_disciplina):
    maior = matriz_notas[indice_disciplina]
    for linha in matriz_notas:
        if linha[indice_disciplina] > maior:
            maior = linha[indice_disciplina]
    return maior

# 3. Função para gerar o relatório final formatado
def exibir_relatorio(alunos, matriz_notas):
    medias = calcular_medias(matriz_notas)

    print("\n" + "=" * 55)
    print(f"{'ALUNO':<15} | {'NOTAS':<15} | {'MÉDIA':<7} | {'SITUAÇÃO'}")
    print("=" * 55)

    for i in range(len(alunos)):
        nome = alunos[i]
        # Formata a lista de notas do aluno para exibição
        notas_str = " ".join([f"{n:.1f}" for n in matriz_notas[i]])
        media = medias[i]
        situacao = "Aprovado" if media >= 7.0 else "Reprovado"

        print(f"{nome:<15} | {notas_str:<15} | {media:<7.1f} | {situacao}")

    print("=" * 55)

# --- PROGRAMA PRINCIPAL ---

# Vetor com o nome dos alunos
alunos = ["Ana", "Bruno", "Carla", "Diego"]

# Matriz 4x3: 4 alunos (linhas) e 3 disciplinas (colunas: Mat, Port, Hist)
matriz_notas = [
    [8.5, 7.0, 9.0],  # Notas da Ana
    [5.0, 6.0, 4.5],  # Notas do Bruno
    [9.0, 9.5, 8.0],  # Notas da Carla
    [6.0, 7.5, 8.0],  # Notas do Diego
]

# Exibição do relatório
exibir_relatorio(alunos, matriz_notas)

# Consulta de maior nota na disciplina 0 (Matemática)
maior_mat = maior_nota_disciplina(matriz_notas, 0)
print(f"\nA maior nota na disciplina de Matemática foi: {maior_mat:.1f}")
```

---

### **Como os conceitos foram integrados nesse código:**

- **Vetor (`alunos`)**: Uma lista unidimensional contendo os nomes.
- **Matriz (`matriz_notas`)**: Uma lista de listas bidimensional (\(4 \times 3\)), onde a posição `matriz_notas[i][j]` acessa a nota do aluno `i` na disciplina `j`.
- **Funções (`def`)**: Reutilização de lógica e separação de responsabilidades (cálculo de média, busca de maior nota e exibição do relatório).