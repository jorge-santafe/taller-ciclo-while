a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))

i = a +1

if i>= b: 
    print("No hay enteros interiores")
else:
    while i< b:
        print(i)
        i+= 1