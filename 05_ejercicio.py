while True:
    capital = int(input("Ingrese el capital inicial: "))
    tasa_anual = int (input("Ingrese tasa anual: "))
    anios = int (input("Ingrese cantidad de años: "))

    if capital >=0 and 0<tasa_anual and tasa_anual<100 and anios>=0:
        break

saldo= capital

i = 1
while i <= anios:
    saldo = saldo * (1 + tasa_anual/100)
    print ("Saldo al terminar año ", i ,": ",saldo )
    i+=1

print("Saldo final: ", saldo)