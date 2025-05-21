matriz= [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]
def imprimir_tablero(tablero):
    for fila in tablero:
        print("". join (str(celda) for celda in fila))
        print()
def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas= len(tablero[0])
    nueva= [[0 for _ in range(columnas)] for _ in range (filas)]
    for i in range(filas):
        for j in range(columnas):
            vecino=0
            if j> 0:
                vecino += tablero[i] [j-1]
            if j< columnas -1 :
                vecino += tablero[i] [j+1]
            if  tablero [i][j]==1:
                if vecino ==1 or vecino==2:
                    nueva [i][j] = 1
                else: 
                    nueva [i][j]=0
            else:
                if vecino==1:
                    nueva[i][j]=1
                else: nueva [i][j]=0
    return nueva            
print("Generacion 0: ")
print("")
imprimir_tablero(matriz)
generacion1= siguiente_generacion(matriz)
print("Generacion 1: ")
print("")
imprimir_tablero(generacion1)
generacion2= siguiente_generacion(generacion1)
print("Generacion 2: ")
print("")
imprimir_tablero(generacion2)