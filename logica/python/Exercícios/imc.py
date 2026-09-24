import time

print("Indice de massa corporal")
peso = int (input("Seu peso: "))
altura = float (input("Sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu indice de massa corporal é {imc}!")
time.sleep(3)

if (imc < 17):
    print("Você está muito abaixo do peso")
elif (imc >= 17) and (imc < 18.5):
    print("Você está no peso ideal")
elif (imc >= 25) and (imc < 30):
    print("Você está em sobrepeso")
elif (imc >= 30) and (imc < 35):
    print("Você está obeso")
elif (imc >= 35) and (imc < 35):
    print("Você está em obesidade severa")
else:
    print("Você está em obesidade morbida")