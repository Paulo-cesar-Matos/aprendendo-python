IDENTIFICADORES
1. Deve começar com uma letra
2. Os próximos podem ser letras ou números
3. Não pode utilizar nenhum símbolo, exceto `_`(underline)
4. Não pode conter espaços em branco
5. Não pode conter letras com acentos
6. Não pode ser uma palavra reservada
Exemplos:
	Nota1 = sim
	Inicio_Algoritmo = sim
	Média = não
	Salário bruto = não
	9idade = não
	Algoritmo = não
	
Tipagens para variáveis
Em Python, os tipos primitivos mostrados na imagem correspondem aos seguintes tipos de dados básicos:
Inteiro (int): Armazena números inteiros, sejam positivos, negativos ou zero.
	Exemplo: idade = 25, temperatura = -5

Real (float): Armazena números reais (com ponto flutuante/casas decimais).
	Exemplo: altura = 1.75, pi = 3.1415

Caractere / Texto (str): Armazena sequências de caracteres (textos), delimitados por aspas simples ou duplas. Em Python, não existe um tipo separado apenas para um único caractere; tudo é tratado como string (str).
	Exemplo: nome = "Gustavo", curso = "Algoritmo"

Lógico (bool): Armazena valores de verdadeiro ou falso. Em Python, eles são representados pelas palavras reservadas `True` e `False` (sempre com a primeira letra maiúscula).
	Exemplo: aprovado = True, visível = False


Expliação somas.py
                    n1 = 5
                    n2 = 2
+ = adição                          (n1 + n2)       = 7
- = subtração                       (n1 - n2)       = 3
* = multiplicação                   (n1 * n2)       = 10
/ = divisão real                    (n1 / n2)       = 2.5
f"\\" = divisão interna             (n1 f"\" n2)    = 2
** = exponenciação/potência         (n1 ^ n2)       = 25
% = módulo                          (n1 % n2)       = 1

                ordem de precedencia
() = parênteses                         3 + 2 / 2       = 4
^ = exponenciação                       (3 + 2) / 2     = 2.5
* / = multiplicação e divisão
+ - = adição e subtração

**FUNÇÕES ARITMÉTICAS**

| Função | O que faz | Exemplo | Resultado |
| --- | --- | --- | --- |
| **Abs** | Valor Absoluto | `Abs(-10)` | `10` |
| **Exp** | Exponenciação | `Exp(3,2)` | `9` |
| **Int** | Valor Inteiro | `Int(3.9)` | `3` |
| **RaizQ** | Raiz Quadrada | `RaizQ(25)` | `5` |
| **Pi** | Retorna Pi | `Pi` | `3.14..` |
| **Sen** | Seno (rad) | `Sen(0.523)` | `0.5` |
| **Cos** | Cosseno (rad) | `Cos(0.523)` | `0.86` |
| **Tan** | Tangente (rad) | `Tan(0.523)` | `0.57` |
| **GrauPRad** | Graus para Rad | `GrauPRad(30)` | `0.52` |vv


**OPERADORES LÓGICOS**

| p   | q   | p E q |
| --- | --- | ----- |
| V   | V   | V     |
| V   | F   | F     |
| F   | V   | F     |
| F   | F   | F     |
|
| V | F | F

| p   | q   | p OU q |
| --- | --- | ------ |
| V   | V   | V      |
| V   | F   | V      |
| F   | V   | V      |
| F   | F   | F      |

| P   | NÃO q |
| --- | ----- |
| V   | F     |
| F   | V     |

**ORDEM DE PRECEDÊNCIA**

| Categoria | Operadores |
| --- | --- |
| **Aritméticos** | `()` |
|  | `^` |
|  | `* /` |
|  | `+ -` |
| **Relacionais** | **Todos** |
| **Lógicos** | `E` |
|  | `OU` |
|  | `NÃO` |