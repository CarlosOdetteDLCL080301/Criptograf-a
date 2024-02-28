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

# Creamos una función para cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        # Comprobamos que sea una letra
        if letra.isalpha(): 
            # Comprobamos si es mayúscula
            if letra.isupper(): 
                # Convertimos la letra a un número entre 0 y 25
                codigo = ord(letra) - ord('A') 
                # Aplicamos el desplazamiento considerando que si se pasa de 25 debe volver a empezar
                codigo = (codigo + desplazamiento) % 26
                # Convertimos el número resultante a letra y lo añadimos al texto cifrado 
                resultado += chr(codigo + ord('A')) 
            else:
                # Comprobamos que sea una letra
                codigo = ord(letra) - ord('a')
                # Aplicamos el desplazamiento considerando que si se pasa de 25 debe volver a empezar
                codigo = (codigo + desplazamiento) % 26
                # Convertimos el número resultante A letra y lo añadimos al texto cifrado
                resultado += chr(codigo + ord('a'))
        else:
            # Si no es una letra lo añadimos tal cual
            resultado += letra 
    # Retornamos el texto cifrado
    return resultado

#Se recibe la cadena que se desea cifrar
texto_original = "Por mi raza hablara el espiritu"
# Se recibe una llave
llave = "DELACRUZLOPEZ"
# Si la llave, tiene letras repetidas, se eliminan para reducir las posibilidades de cifrarlo
texto_limpio = limpiarCadena(llave)
# Se recorre la llave para cifrar el texto con cada letra de la llave
for letraLlave in texto_limpio:
    # Se verifica que la letra sea una letra
    if letraLlave.isalpha():
        # Se obtiene el desplazamiento de la letra
        desplazamiento = ord(letraLlave) - ord('A') if letraLlave.isupper() else ord(letraLlave) - ord('a')
        # Se cifra el texto con el desplazamiento obtenido
        texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
        # Se imprime el texto cifrado
        print(f"El texto ''{texto_original}'' cifrado con la llave {letraLlave} es: '{texto_cifrado}'")
