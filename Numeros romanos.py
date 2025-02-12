print("Bienvenido ")
valor=int(input("Ingrese un numero que este entre 1-9: "))
resultado=''
if valor<=3:
    resultado=valor*'I'
elif valor==9:
    resultado=(valor-8)*'I'+'X'
elif valor>=5:
    resultado=(valor-5)+'V'*'I'
elif valor==4:
    resultado= 'IV'
    print("el valor de ", valor, "en numeros romanos es: ", resultado)
else:
    print("El numero que se ingreso es incorrecto")