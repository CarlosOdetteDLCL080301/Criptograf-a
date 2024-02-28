def limpiarCadena(llave):
    for letra in llave:
        l = llave.find(letra)
        mantener = llave[:l+1]
        modificar = llave[l+1:]
        modificar= modificar.replace(letra, "")
        llave = mantener + modificar
    return llave

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha(): # Comprobamos que sea una letra
            if letra.isupper(): # Comprobamos si es mayúscula
                codigo = ord(letra) - ord('A') # Convertimos la letra a un número entre 0 y 25
                codigo = (codigo + desplazamiento) % 26 # Aplicamos el desplazamiento considerando que si se pasa de 25 debe volver a empezar
                resultado += chr(codigo + ord('A')) # Convertimos el número resultante a letra y lo añadimos al texto cifrado
            else:
                codigo = ord(letra) - ord('a')# Comprobamos que sea una letra
                codigo = (codigo + desplazamiento) % 26# Aplicamos el desplazamiento considerando que si se pasa de 25 debe volver a empezar
                resultado += chr(codigo + ord('a'))# Convertimos el número resultante A letra y lo añadimos al texto cifrado
        else:
            resultado += letra # Si no es una letra lo añadimos tal cual
    return resultado

#Se recibe la cadena
texto_original = "aA bB cC"
llave = "DELACRUZLOPEZ"
texto_limpio = limpiarCadena(llave)
print(texto_limpio)
for letraLlave in llave:
    if letraLlave.isalpha():
        desplazamiento = ord(letraLlave) - ord('A') if letraLlave.isupper() else ord(letraLlave) - ord('a')
        print(desplazamiento)
        texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
        print(f"El texto {texto_original} cifrado con la llave {letraLlave} es: {texto_cifrado}")
