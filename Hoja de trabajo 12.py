# Número de días a registrar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
# Datos simulados de 1 semana de paciente
niveles_azucar = [130, 160, 95, 175, 160]
niveles_sal = [2000, 2400, 1800, 2400, 2700] 
presion_sistolica = [115, 130, 110, 125, 175]
presion_diastolica= [75, 78, 70, 72, 90]
for i in range(len(dias)):
    azucar = niveles_azucar[i]
    sal= niveles_sal[i]
    sistolica= presion_sistolica[i]
    diastolica= presion_diastolica [i]
    
    if azucar[i] >=72 and azucar[i]<=120:
        print("Su nivel de azucar es saludable")
    else:
        ("nivel de azucar fuera de rango")
    if sal <= 2300:
        print("Su consumo de sal es saludable")
    else:
        print("Su consumo de sal esta fuera del rango")
    if sistolica <120 and diastolica <80:
        print("normal")
    elif sistolica >=120 and sistolica <=129 and diastolica <80:
        print("Elevada")
    elif sistolica >130 and sistolica <139 and diastolica >80 and diastolica < 89:
        print("Hipertension tipo 1")