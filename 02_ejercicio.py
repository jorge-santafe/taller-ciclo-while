numero = int(input("Ingrese un numero: "))

LIMITE= -50
suma = 0
while numero != LIMITE:
    suma += numero
    numero = int(input("Ingrese un numero: "))

print("Suma:", suma)