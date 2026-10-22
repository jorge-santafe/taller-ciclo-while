print('''
Para finalizar el proceso ingrese -99 como nota
''')
nota = float(input("Ingrese una nota: "))

suma=0
cantidad = 0

while nota!= -99:
    suma+=nota
    cantidad+=1
    nota= float(input("Ingrese nota: "))

print ("Cantidad de notas: ", cantidad)

if cantidad > 0: 
    promedio = suma / cantidad
    print("Promedio: ", promedio)
else:
    print("Sin notas")