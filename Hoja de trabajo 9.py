#Ejercicio 1
#num=int(input("Ingrese un numero "))
#def es_par_o_impar(num):
    #if num%2==0:
   #     print("El numero es par")
  #  else:
 #       print("El numero es impar")
#es_par_o_impar(num)

#Ejercicio 2
#lis=input("Ingrese su lista ").split()
#def suma_lista(lis):
    #suma=0
   # for numero in lis:
  #      suma+= int(numero)
 #   print(suma)
#suma_lista(lis)

#Ejercicio 3
#num=int(input("Ingrese un numero "))
#def cuenta_regresiva(num):
    #if num<0:
    #    print("¡¡DESPEGANDO!!")
   # else:
  #      print(num)
 #       cuenta_regresiva(num -1)
#cuenta_regresiva(num)

#Ejercicio 4
def cuenta_ascendente(i, x):
    if i == x:
        print("¡lLegaste al numero!")
    else:
        print(i)
        cuenta_ascendente(i + 1, x)
n = int(input("Ingrese el número hasta el que cuenta: "))
cuenta_ascendente(1, n +1)