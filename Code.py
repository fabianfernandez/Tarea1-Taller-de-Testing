import time

print("Hola, ingresa la cadena de caracteres: ",end="")
cadena = input()

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

print(output)
