import math # tem que importar os módulos do python para que o código não fique cheio de gambiarras
import time

print("Funções aritméticas")
time.sleep(3)

# valor absoluto
val_ab = float (input("Valor absoluto. Informe um número: "))
print(f"O valor absoluto de {val_ab} é {abs(val_ab)}")
time.sleep(3)

# raiz quadrada
num = float (input("Raiz quadrada. Informe um número: "))
raiz = math.sqrt(num)
print(f"O resultado é {raiz}")
time.sleep(3)

# graus para radianos
graus = float (input("Graus para radianos. Informe um número: "))
rad = math.radians(graus)
print(f"O resultado é {rad}")
time.sleep(3)

# seno cosseno tangente
cat_op = int (input("Informe o cateto oposto: "))
cat_ad = int (input("Informe o cateto adjacente: "))
h = int (input("Informe a hipotenusa: "))

sen = cat_op/h
cos = cat_ad/h
tan = cat_op/cat_ad

time.sleep(3)

print("Segue os resultados abaixo")
print(f"Seno: ", sen)
print(f"CosSeno: ", cos)
print(f"Tangente: ", tan)

time.sleep(3)