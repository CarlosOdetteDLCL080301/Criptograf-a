import string

# Generamos el mapeo de letras con Ñ 
#alfabeto =string.ascii_uppercase[:14]+"Ñ"+string.ascii_uppercase[14:]+" "
# Generamos el mapeo de letras sin Ñ 
alfabeto =string.ascii_uppercase+" "

def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

def modular_inverse(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        # No hay inverso modular si a y m no son coprimos
        raise ValueError(f"{a} y {m} no son coprimos, no existe inverso modular.")
    else:
        return x % m

# Creamos una función para cifrar un mensaje con el algoritmo de cifrado afín
# ahora solo esta adaptado para cifrar en mayusculas
def cifradoAfin(a,b,mensaje):
    global alfabeto
    # Ciframos el mensaje con la formula (a*mensaje + b) mod len(alfabeto)
    cifrar = (a*alfabeto.find(mensaje) + b) % len(alfabeto)
    # Retornamos la letra cifrada
    return alfabeto[cifrar]
# Creamos una función para descifrar un mensaje con el algoritmo de cifrado afín
def descrifrarAfin(a,b,cifrado):
    global alfabeto
    # Desciframos el mensaje con la formula invMod(a,len(alfabeto))(cifrado - b) mod len(alfabeto)
    return alfabeto[(alfabeto.find(cifrado)-b)*modular_inverse(a,len(alfabeto))%len(alfabeto)]

# Función principal
def main():
    # El mensaje a cifrar, puede ser cualquier caracter, 
    mensajeCifrar = input("Ingrese el mensaje a cifrar: ")                   
    a = int(input("Ingrese el valor de la constante de multiplicación a: "))
    b = int(input("Ingrese el valor de la constante de desplazamiento b: "))
    mensajeCifrado = ""
    mensajeDescifrado = ""
    for letra in mensajeCifrar:
        mensajeCifrado+=cifradoAfin(a,b,letra.upper())
    for letra in mensajeCifrado:
        mensajeDescifrado+=descrifrarAfin(a,b,letra.upper())
    print(f"".center(50,"="))
    print(f" Datos de entrada ".center(50,"="))
    print(f"".center(50,"="))
    print(f"Mensaje a cifrar: {mensajeCifrar}")
    print(f"Valor de la constande de multiplicación a: {a}")
    print(f"Valor de la constande de desplazamiento b: {b}")
    print(f"".center(50,"="))
    print(f" Datos de Salida ".center(50,"="))
    print(f"".center(50,"="))
    print(f"Mensaje cifrado: {mensajeCifrado}")
    print(f"Mensaje descifrado: {mensajeDescifrado}")

main()