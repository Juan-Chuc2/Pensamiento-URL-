#primer ejercicio
#entrada="python es un lenguaje poderoso"
#new=entrada.split()
#a=len(new)
#primera_palabra=new[0]
#print(primera_palabra)
#ultima_palabra=new[4]
#print(ultima_palabra)

#segundo ejercicio
#entrada="Hola   mundo  en python"
#new=entrada.split()
#a=" ".join(new)
#print(a)

#Tercer ejercicio 
#entrada="usuario@gmail.com"
#new=entrada.split('@')
#otro=new[1]
#print(otro)

#-cuarto ejercicio 
#entrada="Documento.jpg"
#salida=entrada.endswith(".pdf")
#print(salida)

#quinto ejercicio
#entrada="Me Gusta Python"
#new=entrada.split()
#a=new[::-1]
#b=" ".join(a)
#print(b)

# Sexto ejercicio 
entrada=input("Hola que Como puedo ayudarte")
poema1="""Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podrá romperse el eje de la tierra Como un débil cristal."""
poema2="En tus ojos encuentro mi paz,en tu sonrisa, mi felicidad. Eres el sol que ilumina mi alma,y el amor que siempre me calma"
poema3= "El viento susurra entre las hojas,el río canta su melodía.La montaña se alza majestuosa, y el cielo se pinta de mil colores"
canto1="Verde prado, azul cielo, canta el río, vuela el viento. Montañas altas, flores bellas, la naturaleza nos cuenta estrellas"
canto2= "Aunque la noche sea oscura, siempre hay una estrella que fulgura. No pierdas la fe, no te rindas, la esperanza siempre nos brinda"
if entrada in poema1:
    print("Claro aquí tienes uno:",poema1)
elif entrada in poema2:
    print("Claro aquí tienes uno:",poema2)
elif entrada in poema3:
    print("Claro aquí tienes uno:", poema3)
elif entrada in canto1:
    print("Claro aqui tienes uno:",canto1)
elif entrada in canto2:
    print("Claro aqui tienes uno:", canto2)
else:
    print(" Mil disculpas no tengo nada relacionado a lo solicitado")