num=int(input("ingrese un numero de 5 digitos "))
a=0
b=0
c=0
d=0
e=0
if num>=10000 and num<1000000:
    print("es valido ")
a=num//10000  
b=(num%10000)//1000
c=(num//10000)%1000
d=(num%100)//10 
e=num%10
if a>b:
else:
    print("no es valido ")