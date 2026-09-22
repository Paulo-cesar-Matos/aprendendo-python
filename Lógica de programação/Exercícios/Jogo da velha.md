### **Exercício 2: Jogo da Velha (Matrizes e Funções)**

**Desafio:** Implementar um **Jogo da Velha** interativo para dois jogadores (`X` e `O`) usando uma matriz \(3 \times 3\).

```
# Inicializa a matriz 3x3 com as posições de 1 a 9
tabuleiro = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def exibir_tabuleiro(t):
    print("\n")
    for linha in t:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(t, simbolo):
    # Verifica linhas e colunas
    for i in range(3):
        if all(t[i][j] == simbolo for j in range(3)): return True
        if all(t[j][i] == simbolo for j in range(3)): return True
    # Verifica diagonais
    if t == t == t == simbolo: return True
    if t == t == t == simbolo: return True
    return False

# Loop do Jogo
jogador_atual = "X"
jogadas = 0

while jogadas < 9:
    exibir_tabuleiro(tabuleiro)

    posicao = input(f"Jogador [{jogador_atual}], escolha uma posição (1-9): ")

    if not posicao.isdigit() or not (1 <= int(posicao) <= 9):
        print("Entrada inválida! Escolha de 1 a 9.")
        continue

    pos = int(posicao) - 1
    linha = pos // 3
    coluna = pos % 3

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("⚠️ Posição já ocupada! Tente outra.")
        continue

    tabuleiro[linha][coluna] = jogador_atual
    jogadas += 1

    if verificar_vitoria(tabuleiro, jogador_atual):
        exibir_tabuleiro(tabuleiro)
        print(f"\n🎉 Parabéns! O jogador [{jogador_atual}] venceu!")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"
else:
    exibir_tabuleiro(tabuleiro)
    print("\n🤝 Empate! Deu Velha!")
```
