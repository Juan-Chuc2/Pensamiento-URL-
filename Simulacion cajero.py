# Se da un saldo Realizar una simulacion de cajero
saldo=3000
intentos=0
while True:
    retiro=int(input("Ingrese el monto que desea retirar "))
    if retiro==0:
        print("Beep Beep... Adios")
        break
    elif retiro>saldo:
        print("Beep Beep... Saldo insuficiente ")
        intentos= intentos+ 1
    if intentos==3:
        print("Beep Beep... demasiados intentos fallidos")
        break
    else:
        saldo= saldo-retiro 
        print("Beep Beep... Retiro exitoso, Su saldo final es de: ", saldo)
        print("Estimado usuario si ya no desea efectuar otra transaccion ingrese 0 para salir")
