print("Para salir del programa ingrese como salario el valor de cero.\n")
salario = int(input("Ingrese el salario mensual:"))

trabajador = 0
while salario !=0 :
    dias = int(input("Ingrese dias trabajados: "))
    bonos = int(input("Ingrese bonos:  "))
    otras_deducciones = int(input("Ingrese otras deducciones: "))

    salario_proporcional = salario * dias /30
    salario_devengado = salario + bonos
    salario_neto = salario_devengado * 0.83 -otras_deducciones

    trabajador += 1
    print("Pago neto trabajador", trabajador, ": ", salario_neto)
    salario = int(input("Ingrese el salario mensual:"))

if trabajador == 0:
    print("Sin trabajadores")