import string

#Función para limpiar la llave, eliminando las palabras que se repiten
def limpiarCadena(llave):
    #Recorremos la llave letra por letra
    for letra in llave: 
        #Buscamos la letra en la llave
        l = llave.find(letra) 
        #Guardamos la parte de la llave que no se va a modificar considerando a partir del punto de referencia para no modificar la llave
        mantener = llave[:l+1] 
        # Guardamos la parte de la llave que se va a modificar considerando a partir del punto de referencia
        modificar = llave[l+1:]  
        #Eliminamos la letra que se repite
        modificar= modificar.replace(letra, "")
        #Unimos las dos partes de la llave
        llave = mantener + modificar
    #Regresamos la llave limpia
    return llave

# Creamos una función para crear un mapa del abecedario con una llave
def crearMapaAbecedario(llave):
    return limpiarCadena(llave+string.ascii_lowercase+string.ascii_uppercase)

# Creamos una función para cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento, mapaLlave):
    resultado = ""
    for letra in texto:
        # Comprobamos que sea una letra
        if letra.isalpha(): 
            # Obtenemos el índice de la letra en el mapa
            indiceEnMapa = mapaLlave.find(letra)
            resultado += mapaLlave[(indiceEnMapa + desplazamiento) % len(mapaLlave)]
        else:
            # Si no es una letra lo añadimos tal cual
            resultado += letra 
    # Retornamos el texto cifrado
    return resultado

#Se recibe la cadena que se desea cifrar
texto_original = "Por mi raza hablara el espiritu"
# Se recibe una llave
llave = "Por mi raza hablara el espiritu"
# Se recibe el desplazamiento
desplazamiento = 3
# Se crea el mapa del abecedario con la llave
#mapaLlave = string.ascii_lowercase+string.ascii_uppercase
mapaLlave = crearMapaAbecedario(llave)
# Se cifra el texto con el desplazamiento obtenido
texto_cifrado = cifrado_cesar(texto_original, desplazamiento, mapaLlave)
dimensionImpresion = 150
print(f"".center(dimensionImpresion, "="))
print(f"Mapa utilizado: {mapaLlave}".center(dimensionImpresion, " "))
print(f"".center(dimensionImpresion, "="))
# Se imprime el texto 
print(f"".center(dimensionImpresion, "#"))
print(f"El texto ''{texto_original}'' cifrado con la llave {desplazamiento} es: '{texto_cifrado}'".center(dimensionImpresion, " "))
print(f"".center(dimensionImpresion, "#"))
