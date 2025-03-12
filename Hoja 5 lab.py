# primer ejercicio 
#agua= int(input("ingrese la cantidad de metros cubicos "))
#if agua<15:
 #   print("La tarifa es Q5 por m³", (5*agua))
#elif agua >=15 and agua <=30:
#    habitantes= int(input("ingrese el numero de habitantes "))
#    if habitantes>3:
     #   print(" la tarifa es Q4 por m³ y su tarifa total es:", (4*agua))
    #elif habitantes ==3:
   #     print(" la tarifa es de Q4.5 por m³ y su tarifa total es:", (4.5*agua))
   # else:
  #      print(" la tarifa es de Q5 por m³ y su tarifa total es:", (5*agua))
#elif agua>30:
    #habitantes= int(input("ingrese el numero de habitantes "))
    #    print(" la tarifa es de Q3.5 por m³ y su tarifa total es:", (3.5*agua))
    #elif habitantes%2 ==0:
    #    print("la tarifa es de Q4 por m³ y su tarifa total es:", (4*agua))
   # else: 
       # print("la tarifa es de Q4.2 por m³ y su tarifa total es:", (4.2*agua)) 

#Segundo ejercicio 
año= int(input("ingrese el año de su vehiculo "))
placa= (input("Ingrese las placas de su vehiculo "))
par= ['0','2','4','6','8']
impar=['1','3','5','7','9']
a= año -2025
if año>=2001:
    if (placa[-1]in par ):
        print("no circula los lunes")
    elif (placa[-1] in impar):
        print("no circula los viernes")
if año % 2==0:
    print("los sabados solo circula medio día")
if (2025-año)>25:
    print("⚠️advertencia: mantenimiento obligatorio")