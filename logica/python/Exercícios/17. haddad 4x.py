import time
compra = int (input("Quanto foi isso ai em? R$"))
pagar = (compra * 60) / 100
time.sleep(1)
if compra == 0:
    print("E esse iPnhone ai nas calças? >:)")
elif compra > 0:
    print(f"Você tem que pagar R${pagar:.0f} reais de imposto >:)")
time.sleep(1)