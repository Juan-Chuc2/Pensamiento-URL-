# Ejercicio 1 Veterninaria
# class Animal:
#     def __init__(self, nombre, edad, peso):
#         self.nombre = nombre
#         self.edad = edad
#         self.peso = peso
#     def mostrar_datos(self):
#         print("Nombre:", self.nombre)
#         print("Edad:", self.edad, "años")
#         print("Peso:", self.peso, "kg")
#     def ficha_medica(self):
#         print("Ficha médica del animal")
#         self.mostrar_datos()
# class Perro(Animal):
#     def __init__(self, nombre, edad, peso, raza):
#         super().__init__(nombre, edad, peso)
#         self.raza = raza
#     def calcular_dosis(self):
#         dosis = self.peso * 0.5
#         print("Dosis para perro:", dosis, "ml")
# class Gato(Animal):
#     def __init__(self, nombre, edad, peso, tamaño):
#         super().__init__(nombre, edad, peso)
#         self.tamaño = tamaño
#     def calcular_dosis(self):
#         dosis = self.peso * 0.4
#         print("Dosis para gato:", dosis, "ml")
# class Ave(Animal):
#     def __init__(self, nombre, edad, peso, color ):
#         super().__init__(nombre, edad, peso)
#         self.color = color
#     def calcular_dosis(self):
#         dosis = self.peso * 0.2
#         print("Dosis para ave:", dosis, "ml")
# class Reptil(Animal):
#     def __init__(self, nombre, edad, peso, tipo_escamas):
#         super().__init__(nombre, edad, peso)
#         self.tipo_escamas = tipo_escamas
#     def calcular_dosis(self):
#         dosis = self.peso * 0.3
#         print("Dosis para reptil:", dosis, "ml")
# perro1= Perro("Firulais", 5, 9, "Pitbull" )
# perro1.ficha_medica()
# perro1.calcular_dosis()

# michi= Gato("Kiara", 2, 4, 12)
# michi.ficha_medica()
# michi.calcular_dosis()

# pajare= Ave("Piolin", 2, 0.5, "Amarillo")
# pajare.ficha_medica()
# pajare.calcular_dosis()

# serpiente= Reptil("Draculita", 4, 10, "Escamas gruesas")
# serpiente.ficha_medica()
# serpiente.calcular_dosis()

# Ejercicio 2 Sistema de personas de una institucion 
class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre 
        self.edad = edad
        self.DNI = DNI
    def mostrar_info(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.DNI)
class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, carrera):
        super().__init__(nombre, edad, DNI)
        self.carrera = carrera
    def mostrar_info(self):
        return super().mostrar_info()
        print("carrera: ", self.carrera)
class Profesor(Persona):
    def __init__(self, nombre, edad, DNI, curso, especialidad):
        super().__init__(nombre, edad, DNI)
        self.curso = curso 
        self.especialidad = especialidad
    def mostrar_info(self):
        return super().mostrar_info()
        print("Curso: ", self.curso, "Especialidad: ", self.especialidad)
class Administrativo(Persona):
    def __init__(self, nombre, edad, DNI, departamento_admin):
        super().__init__(nombre, edad, DNI)
        self.departamento_admin = departamento_admin
    def mostrar_info(self):
        return super().mostrar_info()
        print("Departamento Administrativo: ", self.departamento_admin)
print("Estudiante")
estudiante= Estudiante("Juan", 15, 1525, "Computacion")
estudiante.mostrar_info()
print()
print("Profesor")
catedratico= Profesor("Jhoni", 35, 1578, "Matematica", "Algebra")
catedratico.mostrar_info()
print()
print("Administrativo")
admin= Administrativo( "Geovani", 40, 7845,"Gerente")
admin.mostrar_info()