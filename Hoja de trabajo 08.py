# ejercicio 01
#nu= int(input('tamaño array: '))
#m= int(input("multiplos "))
#saida=[]
#for i in range(1, nu +1):
 #   saida.append (i*m)
#print( saida)

#ejrcicio 02
n = int(input("Ingresa la cantidad de clientes: "))
respuestas = []

c = 0
while c < n:
    print("Califica tu servicio recibido:")
    print("5: Excelente")
    print("4: Muy Buena")
    print("3: Buena")
    print("2: Regular")
    print("1: Malo")
    opcion = int(input("Ingresa una de las opciones: "))
    respuestas.append(opcion)
    c = c + 1

conteo = {}
p = 0
while p < n:
    v = respuestas[p]
    if v in conteo:
        conteo[v] = conteo[v] + 1
    else:
        conteo[v] = 1
    p = p + 1

suma = 0
p = 0
while p < n:
    suma = suma + respuestas[p]
    p = p + 1
promedio = suma / n

mayor = 0
frecuencia = 0
p = 0
while p < n:
    v = respuestas[p]
    if conteo[v] > mayor:
        mayor = conteo[v]
        frecuencia = v
    p = p + 1

menor_promedio = 0
p = 0
while p < n:
    if respuestas[p] < promedio:
        menor_promedio = menor_promedio + 1
    p = p + 1

porcentaje = (menor_promedio * 100) / n

print("Respuestas:")
p = 1
while p <= 5:
    if p in conteo:
        print(p, ":", conteo[p])
    else:
        print(p, ":", 0)
    p = p + 1
print("Más frecuente:", frecuencia)
print("Promedio:", promedio)
print("Porcentaje menor al promedio:", porcentaje, "%")
