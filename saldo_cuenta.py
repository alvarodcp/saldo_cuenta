# Lectura de variables
saldo = int(input("Digite el saldo de la cuenta: "))
# Revisión del saldo y disminución del saldo.
while saldo >= 0 :
    retiro = int(input("Digite el monto del retiro: "))
    if retiro <= saldo :
        saldo = saldo - retiro
        print(f"Los fondos disponibles son {saldo}")
    else:
        print(("Fondos insuficientes"))