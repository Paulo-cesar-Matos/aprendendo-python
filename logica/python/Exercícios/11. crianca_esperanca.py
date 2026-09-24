import msvcrt #para as opções do teclado

print(
    '''     CRIANÇA ESPERANÇA
    Muito obrigado por ajudar!
    Tecle o digito correspondente para realizar uma doação
    [1] para doar R$10
    [2] para doar R$25
    [3] para doar R$50
    [4] para doar outros valores'''
) # melhor para ficar com o código limpo

um = "Obrigado por doar R$10 reais :)"
dois = "Obrigado por doar R$25 reais :)"
tres = "Obrigado por doar R$50 reais :)"
grato = "Obrigado por realizar a doação :)"

while True:
    if msvcrt.kbhit():
        tecla = msvcrt.getch().decode('utf-8').lower()
        if tecla == '1':
            print(um)
        elif tecla == '2':
            print(dois)
        elif tecla == '3':
            print(tres)
        elif tecla == '4':
            quatro = input("Qual o valor da doação? R$")
            print(f"Sua doação foi R${quatro} reais")
        break

print(grato)