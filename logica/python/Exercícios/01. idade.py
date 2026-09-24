ano = int (input("Em que ano estamos? "))
ano_nasc = int (input("Em que ano você nasceu? "))
idade = ano - ano_nasc

print(f"Em {ano} você terá {idade} de idade!")

if (idade >= 18):
    print(f" e já terá atingido a maioridade!")