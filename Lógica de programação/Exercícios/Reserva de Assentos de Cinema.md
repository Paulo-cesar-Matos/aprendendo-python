### **Exercício 1: Reserva de Assentos de Cinema (Vetores)**

**Desafio:** Crie um programa para gerenciar a reserva de 10 assentos de uma sala de cinema (identificados de 1 a 10).

- O programa exibe o mapa de assentos (ex: `[ B1 ] [ B2 ] ...`).
- Quando um assento for reservado, seu rótulo muda para `[ X ]`.
- Se o usuário tentar reservar uma cadeira já ocupada, o programa emite um aviso.

```
# Criamos um vetor (lista) com 10 assentos disponíveis
assentos = [f"B{i+1}" for i in range(10)]

def mostrar_cinema(assentos):
    print("\n--- MAPA DA SALA DE CINEMA ---")
    mapa = ""
    for a in assentos:
        mapa += f"[ {a} ] "
    print(mapa)
    print("-" * 40)

while True:
    mostrar_cinema(assentos)

    opcao = int(input("Reserve uma cadeira (1 a 10, ou 0 para sair): "))

    if opcao == 0:
        print("Sessão finalizada. Bom filme!")
        break

    if 1 <= opcao <= 10:
        indice = opcao - 1
        if assentos[indice] == "X":
            print("❌ ERRO: Esse assento já está ocupado!")
        else:
            assentos[indice] = "X"
            print("✅ Assento reservado com sucesso!")
    else:
        print("Opção inválida! Digite um número de 1 a 10.")
```

---

