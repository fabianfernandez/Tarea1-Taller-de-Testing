import time

def log(mensaje):
    FechayHora = time.strftime("%d-%m-%Y %H:%M:%S")
    print(FechayHora +" "+ mensaje)
    return

def main():
    print("Hola, ingresa la cadena de caracteres: ", end ="")
    cadena = input()
    log("Entrada: "+cadena)
    if cadena == "":
        log("Entrada invalida, valor no permitido")
        return 0
    numeroDeCaracteresRepetidos = 0
    cadenaComprimida = ""
    caracterAnalizado = cadena[0]
    for index in range(len(cadena)):
        if caracterAnalizado == cadena[index]:
            numeroDeCaracteresRepetidos +=1
        else:
            cadenaComprimida+= caracterAnalizado + str(numeroDeCaracteresRepetidos)
            numeroDeCaracteresRepetidos = 1
            caracterAnalizado = cadena[index]
    cadenaComprimida+= caracterAnalizado + str(numeroDeCaracteresRepetidos)
    output =""
    if len(cadenaComprimida) > len(cadena):
        output = cadena
    else:
        output = cadenaComprimida
    log("Salida: "+output)
    return 0

main()
