# Ejercicio 1: Simulación de Experimentos de Caída Libre
# import math
# class ExperimentoFisico:
#     def realizar_experimento(self):
#         pass
# class CaidaLibre(ExperimentoFisico):
#     def __init__(self, altura, gravedad):
#         self.altura = altura
#         self.gravedad = gravedad

#     def realizar_experimento(self):
#         if self.altura < 0:
#             return "Error: La altura no puede ser negativa."
#         if self.gravedad == 0:
#             return "Error: La gravedad no puede ser cero."
#         tiempo = math.sqrt((2 * self.altura) / self.gravedad)
#         return "Tiempo de caída: " + str(tiempo)
# altura = float(input("Ingrese la altura (en metros): "))
# gravedad = float(input("Ingrese la gravedad (en m/s^2): "))
# experimento = CaidaLibre(altura, gravedad)
# print(experimento.realizar_experimento())


# Ejercicio 2: Calculadora Científica Personalizada
import math 
class OperacionCientifica:
    def calcular(self):
        return "No se implementó la operación."

class RaizCuadrada(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."
        resultado = math.sqrt(self.numero)
        return "Raíz cuadrada de " + str(self.numero) + ": " + str(resultado)

class Potencia(OperacionCientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        resultado = math.pow(self.base, self.exponente)
        return str(self.base) + " elevado a la " + str(self.exponente) + ": " + str(resultado)

class Logaritmo(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero <= 0:
            return "Error: No se puede calcular el logaritmo de un número no positivo."
        resultado = math.log(self.numero)
        return "Logaritmo natural de " + str(self.numero) + ": " + str(resultado)

class Factorial(OperacionCientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0 or not float(self.numero).is_integer():
            return "Error: El factorial solo está definido para números enteros no negativos."
        resultado = math.factorial(int(self.numero))
        return "Factorial de " + str(int(self.numero)) + ": " + str(resultado)
print("\nOpciones de operación:")
print("1. Raíz Cuadrada")
print("2. Potencia")
print("3. Logaritmo")
print("4. Factorial")
opcion = input("Seleccione una opción (1-4): ")

def es_numero(valor):
    try:
        float(valor)
        return True
    except:
        return False

if opcion == "1":
    numero = input("Ingrese el número: ")
    if es_numero(numero):
        numero = float(numero)
        operacion = RaizCuadrada(numero)
        print(operacion.calcular())
    else:
        print("Entrada inválida.")
elif opcion == "2":
    base = input("Ingrese la base: ")
    exponente = input("Ingrese el exponente: ")
    if es_numero(base) and es_numero(exponente):
        base = float(base)
        exponente = float(exponente)
        operacion = Potencia(base, exponente)
        print(operacion.calcular())
    else:
        print("Entrada inválida.")
elif opcion == "3":
    numero = input("Ingrese el número: ")
    if es_numero(numero):
        numero = float(numero)
        operacion = Logaritmo(numero)
        print(operacion.calcular())
    else:
        print("Entrada inválida.")
elif opcion == "4":
    numero = input("Ingrese el número: ")
    if es_numero(numero):
        numero = float(numero)
        operacion = Factorial(numero)
        print(operacion.calcular())
    else:
        print("Entrada inválida.")
else:
    print("Opción no válida.")