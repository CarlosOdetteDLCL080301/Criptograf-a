from string import ascii_uppercase
# Generamos el mapeo de letras con Ñ
alfabeto = alfabeto =ascii_uppercase[:14]+"Ñ"+ascii_uppercase[14:]+" "

# Realizamos la operación Si: +1 mod 27
def desplazarUno(mensaje):
    global alfabeto
    nuevaCadena = ""
    for letra in mensaje:
        nuevaCadena += alfabeto[(alfabeto.find(letra) + 1)%len(alfabeto)]
    return nuevaCadena

# Realizamos una función para intercambiar un caracter en una cadena con una nueva letra
def reemplazarCaracter(cadena,nuevoCaracter, indice):
    return cadena[:indice] + nuevoCaracter + cadena[indice + 1:]

# Realizamos una función para permutar una cadena segun el patron de permutación
def permutacion(cadena, movimiento):
    nuevaCadena = ""
    for indice in movimiento:
        nuevaCadena += cadena[int(indice) - 1]
    return nuevaCadena

def rellenarCadena(cadena):
    cadena += "X" * (4 - len(cadena) % 4)
    
# Realizamos una función para agregarlo a un arreglo, esto permitiendo la división de la cadena en 4 partes
def agregarAlArreglo(mensaje):
    if len(mensaje) % 4 != 0:
        rellenarCadena(mensaje)
    arreglo = []
    cadena = ""
    contador = 0
    for letra in mensaje:
        cadena += letra
        contador += 1
        if contador == 4:
            arreglo.append(cadena)
            cadena = ""
            contador = 0
    return arreglo

# Realizamos una función para intercambiar los indices del arreglo 
def intercambiarIndices(arreglo):
    if len(arreglo) % 2 == 0:
        for i in range(0, len(arreglo), 2):
            a = arreglo[i]
            b = arreglo[i + 1]
            arreglo[i] = b
            arreglo[i + 1] = a
    return arreglo

# Realizamos una función para cifrar el mensaje con el algoritmo de cifrado lucifer
def cifradoLucifer(mensaje, patronPermutacion, ronda):
    estructura = agregarAlArreglo(mensaje)
    for j in range(ronda):
        if j == ronda - 1:
            estructura = intercambiarIndices(estructura)
        for i in range(0, len(estructura), 2):
            estructura[i] = desplazarUno(estructura[i])
            estructura[i] =  permutacion(estructura[i], patronPermutacion)
    return estructura
    

def main():
    mensaje = "CARLOSODETTEDELACRUZLOPEZ"
    patronPermutacion = "4213"
    ronda = 10
    
    print(f"".center(50,"="))
    print(f" Datos de entrada ".center(50,"="))
    print(f"".center(50,"="))
    print(f"Mensaje a cifrar: {mensaje}")
    print(f"Valor de π: {patronPermutacion}")
    print(f"Valor de rondas: {ronda}")
    print(f"".center(50,"="))
    print(f" Datos de Salida ".center(50,"="))
    print(f"".center(50,"="))
    print(f"Mensaje cifrado: {cifradoLucifer(mensaje, patronPermutacion,ronda)}")

main()