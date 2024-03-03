def decimalABinario(decimal):
    binario = ""
    # Convertimos el decimal a binario
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    # Obtenemos un binario
    binario = str(decimal) + binario
    # Completamos el octeto
    if len(binario) % 8 != 0:
        binario = "0" * (8 - len(binario) % 8) + binario
    return str(decimal) + binario

def binarioADecimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[len(binario) - i - 1]) * 2 ** i
    return decimal

def operacionXOR(binario1, binario2):
    resultado = ""
    for i in range(len(binario1)):
        if binario1[i] == binario2[i]:
            resultado += "0"
        else:
            resultado += "1"
    return resultado

def letraADecimal(letra):
    return ord(letra)

def decimalALetra(numero):
    return chr(numero)

def cifradorVernam(mensaje, clave):
    cifrado = ""
    # Ciframos el mensaje caracter por caracter
    for mensaje, clave in zip(mensaje, clave):
        mensajeBinario = decimalABinario(letraADecimal(mensaje))
        claveBinario = decimalABinario(letraADecimal(clave))
        resultado = operacionXOR(mensajeBinario, claveBinario)
        cifrado += decimalALetra(binarioADecimal(resultado))
    return cifrado

def main():
    mensaje = "hola"
    clave = "FLOR"
    if(not len(mensaje) == len(clave)):
        print("La longitud del mensaje y la clave deben ser iguales")
    else:
        cifrado = cifradorVernam(mensaje, clave)
        print(f"Mensaje Cifrado: {cifrado}")
        mensajeDescifrado = cifradorVernam(cifrado, clave)
        print("Mensaje Descifrado:", mensajeDescifrado)
main()